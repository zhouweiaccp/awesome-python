






## 读取文件
 * 大文件 以反复调用 read(size) 方法， 每次最多读取size个字节的内容
 * 小文件  read()
 * 如果是配置文件， 调用 readlines() 最方便：
 * f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
 
 
 ## StringIO
 数据读写不一定是文件， 也可以在内存中读写  StringIO顾名思义就是在内存中读写str
 
 
 ## BytesIO
 BytesIO实现了在内存中读写bytes
