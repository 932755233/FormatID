import time

from pynput import mouse
from pynput.mouse import Button


mouse = mouse.Controller()

def move():
    mouse.move(-200, 300)

    time.sleep(0.5)

    mouse.position = (34, 41)

    time.sleep(0.5)

    mouse.click(Button.left, 1)


if __name__ == '__main__':
    move()