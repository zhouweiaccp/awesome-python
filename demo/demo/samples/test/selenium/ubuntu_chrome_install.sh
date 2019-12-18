#一、安装Chrome浏览器  https://www.cnblogs.com/x54256/p/8403864.html  https://www.cnblogs.com/w-y-c-m/p/10533361.html
#1、安装依赖
sudo apt-get --fix-broken install -y
sudo apt-get install -y libxss1 libappindicator1 libindicator7
#2、下载Chrome安装包

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#3、安装

sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
#二、安装ChromeDriver
#1、安装xvfb以便我们可以无头奔跑地运行Chrome

sudo apt-get install -y xvfb
#2、安装依赖

sudo apt-get install unzip
#3、下载安装包

wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
#4、解压缩+添加执行权限

unzip chromedriver_linux64.zip
#5、移动

sudo mv -f chromedriver /usr/local/share/chromedriver
#6、建立软连接

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
#三、无头运行Chrome
#1、安装Python依赖

pip3 install selenium

pip3 install pyvirtualdisplay

#2、开干

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))　　# 初始化屏幕
display.start()　　
driver = webdriver.Chrome()　　# 初始化Chrome
driver.get('http://www.cnblogs.com/x54256/')
print driver.title