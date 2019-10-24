Python 3 教程
============https://github.com/michaelliao





## 环境安装
```
#https://blog.csdn.net/sinat_21591675/article/details/82770360
mkdir ~/.pip
cat > ~/.pip/pip.conf<<efo
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
efo
#Windows更换pip/pip3源
#打开目录：%appdata%
#新增pip文件夹，新建pip.ini文件
#给pip.ini添加内容
#[global]
#timeout = 6000
#index-url = https://pypi.tuna.tsinghua.edu.cn/simple
#trusted-host = pypi.tuna.tsinghua.edu.cn
```
pip3 install requirements.txt
pip3 install -r  requirements.txt

## pycharm pip镜像

[url] https://blog.csdn.net/qq_34173549/article/details/81485489
阿里云 http://mirrors.aliyun.com/pypi/simple

  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple

  豆瓣(douban) http://pypi.douban.com/simple

  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple

  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple

[Python进阶](https://github.com/eastlakeside/interpy-zh)