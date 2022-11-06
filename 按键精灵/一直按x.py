import pynput
import time
import pyperclip

from pynput.keyboard import Key
from pynput.mouse import Button



mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()


for i in range(5000):
    time.sleep(4)
    # keyboard.press('x')
    # keyboard.release('x')
    mouse.click(Button.left, 1)  # 点击鼠标事件
    print("111")