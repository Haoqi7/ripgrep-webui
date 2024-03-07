from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import threading
import os
import signal

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", path='/io')

proc = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    global proc
    if proc is not None:
        socketio.emit('message', {'message': '💼💼💼 Busy 💼💼💼\n'})
        return "Busy"

    keyword = request.json['keyword']

    #if '"' in keyword:
    #    socketio.emit('message', {'message': '🚫🚫🚫 Invalid 🚫🚫🚫\n'})
    #    return "Invalid"

    cmd = ['rg', '-uuu', '--smart-case', '--', keyword, '/data']
    proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def get_output():
        global proc
        with app.app_context():
            for line in proc.stdout:
                socketio.emit('message', {'message': line.decode('utf-8')})
        proc = None  # Reset proc
        with app.app_context():
            socketio.emit('message', {'message': '🛑🛑🛑 Done 🛑🛑🛑\n'})

    thread = threading.Thread(target=get_output)
    thread.start()
    socketio.emit('message', {'message': '🚀🚀🚀 Started 🚀🚀🚀\n'})
    return "Started"

@app.route('/cancel', methods=['POST'])
def cancel():
    global proc
    if proc:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        proc = None
    socketio.emit('message', {'message': '❌❌❌ Cancelled ❌❌❌\n'})
    return "Cancelled"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
