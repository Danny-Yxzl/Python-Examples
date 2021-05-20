from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 初始化用户
authorizer = DummyAuthorizer()

# 添加用户：用户名，密码，可访问的路径，拥有的权限（"elradfmwMT"表示全开）
authorizer.add_user(username="username1",
                    password="password1",
                    homedir="E:/dir1/",
                    perm="elradfmwMT")
authorizer.add_user(username="username2",
                    password="password2",
                    homedir="E:/dir2/",
                    perm="elradfmwMT")

# 初始化连接
FTPHandler.authorizer = authorizer

# 监听地址（0.0.0.0监听全部），端口（FTP默认21；报错OSError的话请换端口）
server = FTPServer(("0.0.0.0", 21),
                   FTPHandler)

# 运行
server.serve_forever()
