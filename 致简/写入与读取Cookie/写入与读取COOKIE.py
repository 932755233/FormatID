import time
import datetime
import re

import selenium
from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QFont, QTextCursor
from PySide2.QtWidgets import QApplication, QPushButton, QPlainTextEdit, QTextEdit
from PySide2.QtUiTools import QUiLoader

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainWindow:
    # pte_cookie
    # pte_log
    # cb_browserListSelect
    # but_openBrowser
    def __init__(self):
        self.driver = None
        self.ui = QUiLoader().load('inputandget.ui')

        self.ui.pushButton.setEnabled(False)
        self.ui.but_input.setEnabled(False)
        self.ui.but_clearCK.setEnabled(False)
        # 设置字体
        self.ui.pte_cookie.setFont(QFont("宋体", 12))
        self.ui.pte_log.setFont(QFont("宋体", 12))
        # 设置只读
        self.ui.pte_log.setReadOnly(True)
        # 绑定监听事件
        self.ui.but_openBrowser.clicked.connect(self.openBrowser)


        self.ui.pushButton.clicked.connect(self.tiquCookie)
        self.ui.but_input.clicked.connect(self.inputCookie)
        self.ui.but_clearCK.clicked.connect(self.clearCookie)
        # self.driver = webdriver.Chrome(self.chrome_potions)
        # self.driver = webdriver.Edge(self.chrome_potions)
        # webdriver.Firefox
        # self.driver.get('http://www.baidu.com')

    def openBrowser(self):
        print('openBrowser')
        index = self.ui.cb_browserListSelect.currentIndex()
        print("选择项：" + str(index))
        if index == 0:
            try:
                edge_potions = selenium.webdriver.edge.options.Options()
                edge_potions.add_argument('disable-infobars')
                # 忽略证书错误
                edge_potions.add_argument('--ignore-certificate-errors')
                edge_potions.add_argument('sec-fetch-site=same-site')
                edge_potions.add_experimental_option('useAutomationExtension', False)
                edge_potions.add_experimental_option("excludeSwitches", ['enable-automation'])
                edge_potions.add_argument("--disable-blink-features")
                edge_potions.add_argument("--disable-blink-features=AutomationControlled")
                self.driver = webdriver.Edge(edge_potions)
                self.showLog('打开微软浏览器')
            except:
                self.showLog('未发现微软浏览器')
        elif index == 1:
            try:
                chrome_potions = selenium.webdriver.chrome.options.Options()
                chrome_potions.add_argument('disable-infobars')
                # 忽略证书错误
                chrome_potions.add_argument('--ignore-certificate-errors')
                chrome_potions.add_argument('sec-fetch-site=same-site')
                chrome_potions.add_experimental_option('useAutomationExtension', False)
                chrome_potions.add_experimental_option("excludeSwitches", ['enable-automation'])
                chrome_potions.add_argument("--disable-blink-features")
                chrome_potions.add_argument("--disable-blink-features=AutomationControlled")
                self.driver = webdriver.Chrome(chrome_potions)
                self.showLog('打开谷歌浏览器')
            except:
                self.showLog('未发现谷歌浏览器')
        else:
            try:
                firefox_potions = selenium.webdriver.firefox.options.Options()
                firefox_potions.add_argument('disable-infobars')
                # 忽略证书错误
                firefox_potions.add_argument('--ignore-certificate-errors')
                firefox_potions.add_argument('sec-fetch-site=same-site')
                firefox_potions.add_experimental_option('useAutomationExtension', False)
                firefox_potions.add_experimental_option("excludeSwitches", ['enable-automation'])
                firefox_potions.add_argument("--disable-blink-features")
                firefox_potions.add_argument("--disable-blink-features=AutomationControlled")
                self.driver = webdriver.Firefox(firefox_potions)
                self.showLog('打开火狐浏览器')
            except:
                self.showLog('未发现火狐浏览器')
        self.driver.get('https://www.baidu.com')
        qqq = QPushButton()
        self.ui.pushButton.setEnabled(True)
        self.ui.but_input.setEnabled(True)

    def showLog(self, text):
        print('showLog')
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(date)

        cursor = self.ui.pte_log.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.ui.pte_log.setTextCursor(cursor)
        self.ui.pte_log.insertPlainText(f'{date}---{text}\n')

    def clearCookie(self):
        print('clearCookie')
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.showLog('清除Cookie成功')

    def tiquCookie(self):
        print('tiquCookie')
        # self.driver.switch_to.window(self.driver.window_handles[0])
        cookies = self.driver.get_cookies()
        cookiestr = ''
        for cookie in cookies:
            cookiestr += cookie['name'] + "=" + cookie['value'] + ';'
        self.ui.pte_cookie.setPlainText(cookiestr)
        self.showLog('获取COOKIE')


    def inputCookie(self):
        print('inputCookie')
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        cookieStr = self.ui.pte_cookie.toPlainText()

        cookies = cookieStr.strip().split(';')

        url = self.driver.current_url
        pattern = re.compile('[a-zA-z]+://www.([^\s]*)/')
        print(pattern.search(url).group(1))
        domain = pattern.search(url).group(1)
        for cookiee in cookies:
            # deng = cookiee.split('=')
            print(cookiee)
            if cookiee == '':
                continue
            name = cookiee[:cookiee.index('=')]
            value = cookiee[cookiee.index('=') + 1:]
            # driver.add_cookie({'name': name.strip(), 'value': value.strip()})
            self.driver.add_cookie(
                {'domain': domain, 'httpOnly': False, 'name': name.strip(), 'path': '/', 'sameSite': 'Lax',
                 'secure': True, 'value': value.strip()})
        self.driver.refresh()
        self.showLog('写入COOKIE')


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.ui.show()
    app.exec_()
