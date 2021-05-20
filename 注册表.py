"""
这是一个设置开机启动项的程序。
亲测Python只能操作很少一部分的注册表，其余会报错，原因未知。
警告：修改注册表是高风险行为！
"""
import win32api, win32con


if __name__ == '__main__':
    exePath = "D:/program.exe"

    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                            "Software\Microsoft\Windows\CurrentVersion\Run",
                            0,
                            win32con.KEY_WRITE)
    win32api.RegSetValueEx(key, "PythonTest", 0, win32con.REG_SZ, exePath)

    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                            "Software\Microsoft\Windows\CurrentVersion\Run",
                            0,
                            win32con.KEY_READ)
    print(win32api.RegQueryValueEx(key, "SystemCore"))