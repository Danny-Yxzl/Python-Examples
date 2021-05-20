import os
import time as t
import zipfile


def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)  # 创建zip文件

    for path, dirnames, filenames in os.walk(dirpath):  # 遍历文件
        fpath = path.replace(dirpath, "")  # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩（即生成相对路径）
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


# 第一个是被压缩的文件夹，第二个是zip的保存路径
zipDir("E:/dir0/", "E:/dir0.zip")
