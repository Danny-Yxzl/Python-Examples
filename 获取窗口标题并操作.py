# -*- coding: utf-8 -*-
import os
import time

import win32con
import win32gui

titles = set()


def all_window_title(hwnd, mouse):
    # 获取有图形化界面的窗口的句柄
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        titles.add(win32gui.GetWindowText(hwnd))


win32gui.EnumWindows(all_window_title, 0)
lt = [t for t in titles if t]
lt.sort()


def zhaojb(aa):
    # 根据窗口标题找句柄
    mu = 0
    jh = []
    hwnd_title = dict()

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(
                hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t != "":
            if aa in t:
                jh.append(h)
    if len(jh) == 0:
        print("找不到相应的句柄")
    else:
        return jh


def close_process_by_hwnd(hwnd, _):
    # 根据窗口名关闭进程（无依赖）
    if win32gui.IsWindowVisible(hwnd):
        if name in win32gui.GetWindowText(hwnd):
            win32gui.SetForegroundWindow(hwnd)  # 使当前窗口在最前
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)


if __name__ == "__main__":
    jbid = zhaojb("实例")[0]
    print(jbid)
    win32gui.SetForegroundWindow(jbid)  # 将相应的窗口前置为活动窗口
    time.sleep(2)
