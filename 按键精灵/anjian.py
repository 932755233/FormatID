import pynput
import time
import pyperclip

from pynput.keyboard import Key
from pynput.mouse import Button


def toClip(str):
    pyperclip.copy(str)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(0.5)


# 获取对象
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

# 输出鼠标当前坐标
# print(mouse.position)


index = 2
kuweiNumber = 'STR.Y2.SM'
kuweiName = '圣牧库' + '-%s库位'

# 打开新增窗口
mouse.position = (15, 65)
mouse.click(Button.left, 1)  # 点击鼠标事件

time.sleep(0.5)
# 点击新增窗口的库位名称编辑框
mouse.position = (1309, 728)
mouse.click(Button.left, 1)  # 点击鼠标事件

time.sleep(0.5)
for i in range(index):
    nameStr = kuweiName % (i + 1)
    toClip(nameStr)
    print(nameStr)
    with keyboard.pressed(Key.shift):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    time.sleep(0.5)

    numStr = '000' + str(i + 1)
    numStr = kuweiNumber + '.' + numStr[-4:]
    toClip(numStr)
    print(numStr)
    # 点击保存按钮
    # mouse.position = (1210, 632)
    # mouse.click(Button.left, 1)  # 点击鼠标事件

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    time.sleep(0.5)
