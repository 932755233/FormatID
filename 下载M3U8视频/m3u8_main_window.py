from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from pathlib import Path
import os
import requests
import re

class MainWindow:
    pattern = re.compile(r'[a-zA-z]+://[^\s]*.m3u8', re.I)

    outPath = r'.\output'
    m3u8UrlList = []

    def __init__(self):
        self.ui = QUiLoader().load('m3u8_main_window.ui')
        self.ui.pushButton_start.clicked.connect(self.clickListener)
        self.ui.pushButton_openfolder.clicked.connect(self.openOutputFolder)

    # 打开输出文件夹
    def openOutputFolder(self):
        Path(self.outPath).mkdir(parents=True, exist_ok=True)
        os.startfile(self.outPath)
        self.ui.pushButton_start.setEnabled(True)

    # 开始下载
    def clickListener(self):
        self.makeFolderAndShow()
        self.showOutputInfo('输出文件夹：' + os.path.abspath(self.outPath))
        m3u8AllStr = self.ui.plainTextEdit_m3u8.toPlainText()
        self.m3u8UrlList = self.pattern.findall(m3u8AllStr)
        self.showOutputInfo('解析M3U8链接地址')
        for tempStr in self.m3u8UrlList:
            self.showOutputInfo('  ' + tempStr)
        self.showOutputInfo('共找到%d个' % len(self.m3u8UrlList))

        # 下载
        self.network(self.m3u8UrlList[0])

    def network(self,url):
        ts_rs = requests.get(url).text
        list_content = ts_rs.split('\n')
        for content in list_content:
            print(content)

    # 创建输出文件夹
    def makeFolderAndShow(self):
        self.ui.textBrowser_out.setText('')
        self.ui.pushButton_start.setEnabled(False)
        outPath = self.ui.lineEdit_folder.text()
        if '' != outPath:
            self.outPath = outPath
        Path(self.outPath).mkdir(parents=True, exist_ok=True)

    # 显示输出信息
    def showOutputInfo(self, showStr):
        self.ui.textBrowser_out.append(showStr)
        self.ui.textBrowser_out.moveCursor(self.ui.textBrowser_out.textCursor().End)


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.ui.show()

    app.exec_()
