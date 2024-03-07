import json
import os
import time
import datetime
import re

import requests
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

        self.ui.setWindowTitle("写入与读取COOKIE(可改作用域)")
        self.ui.pushButton.setEnabled(False)
        self.ui.but_input.setEnabled(False)
        self.ui.but_clearCK.setEnabled(False)
        self.ui.but_tongbu.setEnabled(False)
        # 设置字体
        self.ui.pte_cookie.setFont(QFont("宋体", 12))
        self.ui.pte_log.setFont(QFont("宋体", 12))
        self.ui.le_account_template.setFont(QFont("宋体", 12))
        self.ui.le_zuoyongyu.setFont(QFont("宋体", 12))
        # 设置只读
        self.ui.pte_log.setReadOnly(True)
        # 绑定监听事件
        self.ui.but_openBrowser.clicked.connect(self.openBrowser)

        self.ui.pushButton.clicked.connect(self.tiquCookie)
        self.ui.but_input.clicked.connect(self.inputCookie)
        self.ui.but_clearCK.clicked.connect(self.clearCookie)
        self.ui.but_tongbu.clicked.connect(self.uploadAccount)
        # self.driver = webdriver.Chrome(self.chrome_potions)
        # self.driver = webdriver.Edge(self.chrome_potions)
        # webdriver.Firefox
        # self.driver.get('http://www.baidu.com')
        self.ui.le_account_template.setText("无用户名----1----1----1----")

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
        self.ui.but_clearCK.setEnabled(True)
        self.ui.but_tongbu.setEnabled(True)

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
        print(cookies)
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
        print(url)

        js_hostname = "return window.location.hostname"
        hostname = self.driver.execute_script(js_hostname)
        # hostname = '.qq.com'
        # hostname = '.video.qq.com'

        zuoyongyuStr = self.ui.le_zuoyongyu.text()
        print(zuoyongyuStr)
        if zuoyongyuStr != '':
            hostname = zuoyongyuStr

        print("hostname:" + hostname)

        # pattern = re.compile('[a-zA-z]+://www.([^\s]*)/')
        # print(pattern.search(url).group(1))
        domain = hostname
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

    def uploadAccount(self):
        accountTemplate = self.ui.le_account_template.text()
        cookieStr = self.ui.pte_cookie.toPlainText()
        if accountTemplate == '':
            self.showLog('中间模板不能为空')
            return
        if cookieStr == '':
            self.showLog('COOKIE不能为空')
            return

        self.showLog('拼接字符串')
        accountText = accountTemplate + cookieStr
        self.showLog(accountText)

        os.system('echo %s | clip' % accountText)
        self.showLog('账号字符串已复制到剪贴板！')

        self.showLog('开始上传账号')
        self.ui.but_tongbu.setEnabled(False)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/json'
            # 'cookie':'rr=https%3A%2F%2Fcn1.at101.design%2F; iadult=1; hello=1; __cf_bm=p5gOpquFCoj5a8TQG4EXkJgz3Ex7FnsYEfEnocDLOvQ-1672239337-0-Aald4rPN3hah3kmMughmjJnSoAXumWxycfq63F5ZGSO30pHcwtAbqaAZLHGXuYc6q8I0nZgdiJR75WSZ20zsF7Fd02vMkSA7GKGU+aEdw5fSL4rGkP3QLsGEgxf04R5AkhrkKQTrbTGgNWCpGXKzTss=; XSRF-TOKEN=eyJpdiI6ImZObDlvclwvZjN4SnhtMHNyb2NkcTNBPT0iLCJ2YWx1ZSI6InlqNUp4V3dSN2ZucDZYN2h0OExBT2NBMlVFZVpVWXNSUTZuR1NvbVMwMlZhVVJJTDhLNTBnTHIrQUFrNTJJVDIiLCJtYWMiOiI2OGFmNDM5NzE5MDc5ZGFjMTJmODJmYjZkMTVkNWViOGI0YWUyN2JlZjUwZjg2YzEyOTVjZTVjNmZkNmE5NTYzIn0%3D; miao_ss=eyJpdiI6IlZUczhoMFJjN2VhUlRFYis1NXBYZ3c9PSIsInZhbHVlIjoiR2RWRDZncElnemNZa0poTnhGbHNcL1ZoTmlnVDhhNndYcVgxSHFTMCtcL3VnbUVZTXAyWGtCclloaURQR2dwMXVaIiwibWFjIjoiZjBlM2QzZDRjM2FmNzhmZjBmNjliMzgzNGI4NTZiZWEzZmY2MDg5YmJhZDBmNjI5NzJmYzcxMDc0OWNmN2U5YyJ9'
        }

        formdata = {'data': str(accountText), 'type': '1'}

        # urlStr = 'http://192.168.31.155:8086/AccountExternal/addAccount.do'
        urlStr = 'http://47.92.2.81:8080/link/AccountExternal/addAccount.do'
        response = requests.post(urlStr, data=json.dumps(formdata),
                                 headers=headers)
        self.showLog('网络响应：' + response.json()['data'])
        self.ui.but_tongbu.setEnabled(True)

        # self.showLog('上传账号完毕')


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.ui.show()
    app.exec_()

    # 生成exe可执行文件
    # D:\develop\Python\Python38\Scripts\pyinstaller 手动获取验证码.py - Fw