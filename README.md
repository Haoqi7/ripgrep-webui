搜了一圈没找到grep的webui，于是用GPT搓了一个。如果有佬友懒得洗数据搭ELK，又想有个webui的话，可以用用。这东西并发只有1，ripgrep会把核心跑满，并发高了感觉也没用。

## 搭建方法：

0. <strike>首先你得有数据，csv或者txt的那种，哪里下载就不说了🤣</strike> ；
1. 如果你是x86_64的linux，这一步可以忽略：去[ripgrep-release](https://github.com/BurntSushi/ripgrep/releases)下载你系统版本的二进制，比如你是x86_64_linux，就下[ripgrep-14.1.0-x86_64-unknown-linux-musl.tar.gz](https://github.com/BurntSushi/ripgrep/releases/download/14.1.0/ripgrep-14.1.0-x86_64-unknown-linux-musl.tar.gz)，把rg解压出来放到当前目录下;
3. 改docker-compose.yml，把你的社工库目录写进去；
4. `docker-compose build && docker-compose up -d`
5. 浏览器打开: `http://127.0.0.1:5000`

**PS** 查询结果是新的在上面，老的在下面；关闭浏览器标签或者点击取消会杀掉rg进程终止查询。

## 长这样：
<img width="673" alt="image" src="https://github.com/asiojxzcijvi/ripgrep-webui/assets/49741432/33f2ce4d-9fb7-4c16-8d14-7f92b1f17c59">
