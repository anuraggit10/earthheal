# RnD-Python-App-Template
Provides the basic content required to run a Python application in a Docker container.

1. Create Python application.
2. Create Dockerfile
3. Set requirements

## Creating Images with Dockerfiles 

1. Build your image with the build command
```
# docker image build -t new_app .
```
2. Run your container with builded image.
```
# docker container run -d -p 5000:5000/tcp new_app
```

Check if your app is available.
As this is example with python web app, use internet browser and check http://< ip >:5000

3. A helpful commands.

list of images
```
# docker images
```

clear out unneeded docker object
```
# docker image prune
```

remove image
```
# docker image rm ec2f8486f310
```

list of containers
```
# docker container ls
# docker container ls -a
```

remove container
```
# docker container rm 88f61316a519
```

start and stop container
```
docker container run -d -p 5000:5000/tcp new_app
docker container stop 4a95b5bac6ce
```

login in to running container
```
docker exec -ti 8e9c81c680d0 /bin/bash
```

## Set your development environment. 

### Install docker
```
# sudo apt update
# sudo apt install apt-transport-https ca-certificates curl software-properties-common
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
# apt-cache policy docker-ce
# sudo apt install docker-ce
# apt install lvm2 gnupg2 git
# sudo apt install lvm2 gnupg2 git
# sudo usermod -aG docker devops
# docker --version
```

### Install Python

https://www.python.org/downloads/ Here are the commands that we'll run to build and install Python 3:
```
# sudo -i
# apt update -y
# apt install -y \
  wget \
  build-essential \
  libffi-dev \
  libgdbm-dev \
  libc6-dev \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  libncurses5-dev \
  libncursesw5-dev \
  xz-utils \
  tk-dev
```
if centos # yum install openssl-devel zlib-devel wget libffi-devel gdbm-devel
```
# cd /usr/src
# wget http://python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
# tar xf Python-3.7.2.tar.xz
# cd Python-3.7.2
# ./configure --enable-optimizations
# make altinstall
```
#### Note: make altinstall causes it to not replace the built in python executable.

Ensure that secure_path in /etc/sudoers file includes /usr/local/bin. The line should look something like this:
```
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
```
Upgrade Pip (might not be necesary)

The version of pip that we have might be up-to-date, but it's a good practice to try to update it after the installation. We need to use the pip3.7 executable because we're working with Python 3, and we use sudo so that we can write files under the /usr/local directory.
```
# pip3.7 install --upgrade pip
```

Create virtual dev environment for Python
```
# apt-get install python3-venv
# python3 -m venv virtualenvs/my_venv
# source virtualenvs/my_venv/bin/activate
# sudo pip install flask
```
