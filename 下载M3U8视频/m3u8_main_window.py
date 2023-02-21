from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QFileDialog
from PySide2.QtUiTools import QUiLoader
from pathlib import Path
import os
import requests
import re
import threading
import time


class MainWindow:
    pattern = re.compile(r'[a-zA-z]+://[^\s]*.m3u8', re.I)

    def __init__(self):
        self.m3u8UrlList = []
        self.outPath = r'%s\output' % os.getcwd()
        self.ui = QUiLoader().load('m3u8_main_window.ui')
        self.ui.pushButton_start.clicked.connect(self.clickListener)
        self.ui.pushButton_openfolder.clicked.connect(self.openOutputFolderClickListener)
        self.ui.pushButton_jiexi.clicked.connect(self.jiexiClickListener)
        self.ui.pushButton_choose_folder.clicked.connect(self.openChooseFolderClickListener)
        self.ui.lineEdit_folder.setText(self.outPath)
        self.ui.pushButton_start.setEnabled(False)

    # 打开输出文件夹
    def openOutputFolderClickListener(self):
        Path(self.outPath).mkdir(parents=True, exist_ok=True)
        os.startfile(self.outPath)

    # 打开路径选择
    def openChooseFolderClickListener(self):
        self.outPath = QFileDialog.getExistingDirectory(self.ui, '选择输出文件夹')
        self.ui.lineEdit_folder.setText(self.outPath)

    # 解析文本中的所有m3u8链接地址
    def jiexiClickListener(self):
        self.makeFolderAndShow()
        self.showOutputInfo('输出文件夹：' + os.path.abspath(self.outPath))
        m3u8AllStr = self.ui.plainTextEdit_m3u8.toPlainText()
        self.m3u8UrlList = self.pattern.findall(m3u8AllStr)
        self.showOutputInfo('解析M3U8链接地址')
        for tempStr in self.m3u8UrlList:
            self.showOutputInfo('  ' + tempStr)
        self.showOutputInfo('共找到%d个' % len(self.m3u8UrlList))
        if len(self.m3u8UrlList) > 1:
            self.ui.pushButton_start.setEnabled(True)
        else:
            self.ui.pushButton_start.setEnabled(False)

    # 开始下载
    def clickListener(self):

        t = threading.Thread(target=self.network_thread)
        t.start()

        # 下载
        # self.network(self.m3u8UrlList[0])

    def network_thread(self):

        resptext = requests.get(self.m3u8UrlList[0]).text
        list_content = resptext.split('\n')

        if '#EXTM3U' not in resptext:
            print('这不是m3u8视频链接')
            return False
        # 使用re正则得到key和视频地址
        jiami = re.findall('#EXT-X-KEY:(.*)\n', resptext)
        if len(jiami) == 0:
            key = re.findall('URI="(.*)"', jiami[0])
        print(jiami)
        print(key)

    # 创建输出文件夹
    def makeFolderAndShow(self):
        self.ui.textBrowser_out.setText('')
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
