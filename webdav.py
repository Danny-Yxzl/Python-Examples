# pip install webdavclient3

from webdav3.client import Client
from webdav3.exceptions import LocalResourceNotFound

options = {
    'webdav_hostname': "https://pan.bilnn.com/dav",
    'webdav_login': "danny070601@aliyun.com",
    'webdav_password': "PASSWORD",
    'disable_check': True  # 有的网盘不支持check功能
}
client = Client(options)


def upload(file_path, file_name=None):
    file_path = file_path.replace("\\", "/")
    if not file_name:
        file_name = file_path.split("/")[-1]
    try:
        client.upload(file_name, file_path)
        print('Upload at ' + file_name)
    except LocalResourceNotFound as exception:
        print('An error happen: LocalResourceNotFound ---' + file_name)


if __name__ == '__main__':
    print('run upload')
    upload()
