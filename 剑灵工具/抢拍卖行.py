import sys
import time
from system_hotkey import SystemHotkey
from PySide2.QtWidgets import QMainWindow, QApplication, QShortcut
from PySide2.QtGui import QKeySequence
from pymouse import PyMouse
from pykeyboard import PyKeyboard

from ui_qiangshagnchengui import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        self.flag = False

        self.hk_test = SystemHotkey()
        self.hk_test.register(('control', 'f6'), callback=lambda x: self.ui.cb_status.click())

        # shortcut = QShortcut(QKeySequence('+'), self.ui.cb_status)
        # shortcut.activated.connect(self.ui.cb_status.click)

        self.ui.cb_status.stateChanged.connect(self.stateChangedListener)

    def stateChangedListener(self, status):
        print("按键")
        if self.ui.cb_status.isChecked():
            self.ui.cb_status.setText("已开启")
            self.flag = True
        else:
            self.ui.cb_status.setText("已关闭")
            self.flag = False

        self.doTask()


    def doTask(self):
        print("dotask")

        # pydirectinput.mouseDown()
        # time.sleep(0.01)
        # pydirectinput.mouseUp()
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 20, 0)
        # Keyboard.press(0x1e)

        time.sleep(3)
        m = PyMouse()
        k = PyKeyboard()
        k.press_key('1')
        # which you then follow with a release of the key
        k.release_key('1')
        # pydirectinput.mouseDown()
        # pydirectinput.move(50,20)
        # time.sleep(4)
        # pydirectinput.keyDown('w')
        # time.sleep(1)
        # pydirectinput.keyUp('w')
        # keyboard = Controller()
        #
        # keyboard.press('3')
        # keyboard.release('3')
        # while (self.flag):
        #     print("11111")
            # pyautogui.click()
        # pyautogui.rightClick()
        # time.sleep(1)
        # pyautogui.press('a')
        # # 模拟释放键盘的A键
        # pyautogui.release('a')
        print()
        print("dotask---finish")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())

    # 生成exe可执行文件
    # D:\develop\Python\Python38\Scripts\pyinstaller 手动获取验证码.py - Fw
