from ftplib import FTP
from os import device_encoding  #加载ftp模块
ftp = FTP()  #设置变量
ftp.set_debuglevel(2)  #打开调试级别2，显示详细信息
ftp.connect("192.168.31.58", 21)  #连接的ftp sever和端口
ftp.login("username", "password")  #连接的用户名，密码
print(ftp.getwelcome())  #打印出欢迎信息
#print(device_encoding('utf-8'))
ftp.set_debuglevel(0)  #关闭调试模式
ftp.quit()  #退出ftp
