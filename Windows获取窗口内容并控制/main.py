import pygetwindow as gw
import pyautogui as ag
import time

import win32gui
import win32con

window = win32gui.FindWindow(None, "微信")

win32gui.GetDlgItem(window,)

print(window)
print(win32gui.GetClassName(window))
print(win32gui.GetWindowText(window))

# 金蝶EAS-生泰尔数据中心  13177902

def window_enum_callback(hwnd, extra):
    wintext = win32gui.GetWindowText(hwnd)
    winname = win32gui.GetClassName(hwnd)
    print(hwnd, "---", wintext, "---", winname)


win32gui.EnumChildWindows(window, window_enum_callback, None)


# time.sleep(2)

# # 获取当前活动窗口句柄
# hWnd = win32gui.GetForegroundWindow()
#
# # 获取当前焦点窗口句柄
# focused_window = win32gui.GetFocus()
#
# print("当前活动窗口:", hWnd)
# print("当前拥有焦点的窗口:", focused_window)
# print("", win32gui.GetWindowText(hWnd))
# print("", win32gui.GetWindowText(focused_window))
