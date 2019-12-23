#目录
* []()
* []()
* []()
* []()
* []()
* []()



## 1安装

### 1.1 java
### 1.2 Android Sdk
1 http://tools.android-studio.org/index.php/sdk/
2 Path环境变量中添加ANDROID_HOME、tools、platform-tools、build-tools目录。保存修改。
3 在CMD下执行，adb devices，出现下图样式则代表通过adb命令，获取到了连接在电脑上Android手机的UDID
4 安装nodejs ,npm --registry http://registry.cnpmjs.org install -g appium,
cmd 下输入appium -v
4.1  https://bitbucket.org/appium/appium.app/downloads/ 下载安装
appium-doctor   测试
5.pip install Appium-Python-Client
6  D:\Program Files\Nox\bin\    nox_adb.exe connect 127.0.0.1:62001  nox_adb.exe connect 127.0.0.1:62001
安装夜神模拟器的时候那个版本不一致的问题替换了nox_adb.exe之后，输入adb.exe还是报那个kill版本不匹配的错误，着了半天才发现原来在夜神模拟器的bin目录下也有一个adb.exe文件，找到问题所在了
解决办法：简单暴力，将SDK的adb.exe直接替换夜神模拟器bin目录的adb.exe文件
参考地址
* [](http://www.sohu.com/a/283244536_820120)
* [](https://blog.csdn.net/u010381752/article/details/81874273)
* [appium](https://pan.baidu.com/s/4n2MK8Wx)
* [](https://www.cnblogs.com/du-hong/p/10985654.html)  教程中有详细安装
* [特推荐免费的代理小工具蓝灯](https://github.com/getlantern/lantern)  https://www.cnblogs.com/du-hong/p/11003755.html
android sdk 镜像
1、南阳理工学院镜像服务器地址：mirror.nyist.edu.cn     端口：80
2、中国科学院开源协会镜像站地址：
IPV4/IPV6:mirrors.opencas.cn          端口：80
IP4/IPV6:mirrors.opencas.org        端口：80
IPV4/IPV6:mirrors.opencas.ac.cn     端口：80
3、上海GDG镜像服务器地址：sdk.gdgshanghai.com     端口：8000
4、北京化工大学镜像服务器地址：
IPv4:ubuntu.buct.edu.cn/       端口：80
IPv4:ubuntu.buct.cn/              端口：80
IPv6:ubuntu.buct6.edu.cn/     端口：80
5、大连东软信息学院镜像服务器地址：mirrors.neusoft.edu.cn     端口：80