# -*- coding: utf-8 -*-
import urllib.parse
import qrcode

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Sat Dec 21 16:40:19 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QByteArray, QUrl
from PySide2.QtNetwork import QNetworkCookie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("push1Button")
        self.horizontalLayout.addWidget(self.pushButton1)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushBackButton")
        self.horizontalLayout.addWidget(self.pushButton2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.webview = QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.webview.sizePolicy().hasHeightForWidth())
        self.webview.setSizePolicy(sizePolicy)
        self.webview.setObjectName("webview")
        # self.webview.setProperty("User-Agent","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1")
        self.webview.page().profile().setHttpUserAgent(
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1")
        # self.webview.loadFinished.connect(self.update_view)
        self.webview.loadStarted.connect(self.update_view)
        self.webview.page().profile().cookieStore().cookieAdded.connect(self.onCookieAdd)

        self.verticalLayout.addWidget(self.webview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.openUrl)
        self.pushButton1.clicked.connect(self.getUrl)
        self.pushButton2.clicked.connect(self.back)

        self.lineEdit.setText('https://activity.kugou.com/vqq2024/v-1c33c955/index.html?source_id=533001')

    def back(self):
        # self.webview.back()
        htmlstr =''
        self.webview.page().toPlainText(lambda x:print(x))
        print(htmlstr)

    def onCookieAdd(self, cookie):
        # pass
        # cookie = self.webview.page().profile().cookieStore().loadAllCookies()
        # if 'baidu.com' in cookie.domain():
        #     name = cookie.name().data().decode('utf-8')
        #     value = cookie.value().data().decode('utf-8')
        #     if name not in self.DomainCookies:
        #         self.DomainCookies.update({name: value})
        print('onCookieAdd:', cookie.domain(), '\n---', cookie.name().data(), '\n---', cookie.value().data(), sep='')

    def update_view(self):
        url = self.webview.url().url()
        print('update_view:', url)

        # cookies = self.webview.page().profile().cookieStore().loadAllCookies()
        # for cookie in cookies:
        #     print('update_view:', cookie.domain(), '\n---', cookie.name().data(), '\n---', cookie.value().data(), sep='')
        # print(url)
        # web = urllib.parse.urlparse(url)
        # print(web)
        # urlOrigin = QUrl(str(web.scheme + '://' + web.netloc))
        # # urlOrigin = QUrl(str("https://baidu.com"))
        # print(urlOrigin)
        #
        # cookie = ''
        # # cookie = 'STOKEN=bbae6e010d629716e4c5b01f7e93a1839263ba9f3d6f238951e8ea0b04769630; TIEBA_USERTYPE=d7ed3562292cbc4b54c33c9b; csrfToken=x5l3N6uKMxSrGNVczKw4q8h5; PASSID=BTV2Ms; UBI=fi_PncwhpxZ%7ETaKAUbNpclxfCbByIf4FE7uanmMhWFaTEJvfpe2XvKRqWDDuEiUVfrG-N1A96Kuo30sx98PbTh1iU8fQO4H4ZRlxEeOBx-ZHxACJYJyGvvIfC3Z97gJmOmkzAXCiXT8SieQQnhMrRXyseFbYQ__; HOSUPPORT=1; pplogid=7777dNc6pXpdYNgK6lliqVaQvS0GS5y1trR0s1ZzxHMvTqZ4MmmpBh6636z1D5t4wVskRawL5fZh%2BfTItItWfp8nGemLpx9B5AZV5szGaDe5PIBeY0Fl4BUOQUJ1IwZeijKQ; NEWUSER=1; BDUSS=3dnfmlpbVVJSkpvcHV1YXBBfjUxVXM5cFhKS1kyOHRBM01SeTB-Rn5nS1FqVDVsRVFBQUFBJCQAAAAAAQAAAAEAAADsdwyFwNfV89Pq1tXDy7XBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJAAF2WQABdlc; PTOKEN=1b1b8aa2f7603da219cae843ac244175; BAIDUID=AB22C1056526C9224DF99A1C57FB8300:FG=1'
        # # cookie = 'BIDUPSID=D5625B647EC9B0B69BA52E6D7DBAFA31;PSTM=1692628404;BAIDUID=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1;Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34=1704350597,1704352635;H_PS_PSSID=39998_40039;BDSFRCVID=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5;H_BDCLCKID_SF=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P;BDSFRCVID_BFESS=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5;H_BDCLCKID_SF_BFESS=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P;Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1704350597,1704352635,1705030651;Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1705030651;H_WISE_SIDS=39998_40039;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;delPer=0;PSINO=2;BA_HECTOR=2g818h0h0k848501840l8h0hr06j5p1iq1g1m1t;ZFY=1QP1Ms5szl0UB:A70:ABLetAzVoqxEOfql5zZHKc1AGxY:C;BAIDUID_BFESS=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1;ZD_ENTRY=baidu;__bid_n=18a96e4c50a3728a150862;BDUSS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb;BDUSS_BFESS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb'
        # cookie = 'BIDUPSID=D5625B647EC9B0B69BA52E6D7DBAFA31;PSTM=1692628404;BAIDUID=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1;Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34=1704350597,1704352635;H_PS_PSSID=39998_40039;BDSFRCVID=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5;H_BDCLCKID_SF=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P;BDSFRCVID_BFESS=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5;H_BDCLCKID_SF_BFESS=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P;Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1704350597,1704352635,1705030651;Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1705030651;H_WISE_SIDS=39998_40039;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;delPer=0;PSINO=2;BA_HECTOR=2g818h0h0k848501840l8h0hr06j5p1iq1g1m1t;ZFY=1QP1Ms5szl0UB:A70:ABLetAzVoqxEOfql5zZHKc1AGxY:C;BAIDUID_BFESS=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1;ZD_ENTRY=baidu;__bid_n=18a96e4c50a3728a150862;BDUSS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb;BDUSS_BFESS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb'
        #
        # d = self.parse_cookie(cookie)
        # self.webview.page().profile().cookieStore().deleteAllCookies()
        # for key, value in d.items():
        #     cookie_str = QNetworkCookie(QByteArray(key.encode()), QByteArray(value.encode()))
        #     print(cookie_str)
        #     self.webview.page().profile().cookieStore().setCookie(cookie_str, urlOrigin)

    def getUrl(self):
        qurl = self.webview.url()
        print(qurl.url())
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qurl.url())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

    def parse_cookie(self, txt):
        l = txt.split(';')
        d = dict()
        for i in l:
            # t = i.split('=')
            # i.find('=')
            # d[t[0]] = t[1]
            t = i.find('=')
            if t > 0:
                d[i[0:t].strip()] = i[t + 1:]
        return d

    def openUrl(self):
        url = self.lineEdit.text().strip()

        print(url)
        web = urllib.parse.urlparse(url)
        # print(web)
        # urlOrigin = QUrl(str(web.scheme + '://' + web.netloc))
        # print(web.netloc)
        # urlOrigin = QUrl("https://passport.baidu.com")
        # print(urlOrigin)

        cookie = ''
        # cookie = 'STOKEN=bbae6e010d629716e4c5b01f7e93a1839263ba9f3d6f238951e8ea0b04769630; TIEBA_USERTYPE=d7ed3562292cbc4b54c33c9b; csrfToken=x5l3N6uKMxSrGNVczKw4q8h5; PASSID=BTV2Ms; UBI=fi_PncwhpxZ%7ETaKAUbNpclxfCbByIf4FE7uanmMhWFaTEJvfpe2XvKRqWDDuEiUVfrG-N1A96Kuo30sx98PbTh1iU8fQO4H4ZRlxEeOBx-ZHxACJYJyGvvIfC3Z97gJmOmkzAXCiXT8SieQQnhMrRXyseFbYQ__; HOSUPPORT=1; pplogid=7777dNc6pXpdYNgK6lliqVaQvS0GS5y1trR0s1ZzxHMvTqZ4MmmpBh6636z1D5t4wVskRawL5fZh%2BfTItItWfp8nGemLpx9B5AZV5szGaDe5PIBeY0Fl4BUOQUJ1IwZeijKQ; NEWUSER=1; BDUSS=3dnfmlpbVVJSkpvcHV1YXBBfjUxVXM5cFhKS1kyOHRBM01SeTB-Rn5nS1FqVDVsRVFBQUFBJCQAAAAAAQAAAAEAAADsdwyFwNfV89Pq1tXDy7XBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJAAF2WQABdlc; PTOKEN=1b1b8aa2f7603da219cae843ac244175; BAIDUID=AB22C1056526C9224DF99A1C57FB8300:FG=1'
        # cookie = 'BIDUPSID=D5625B647EC9B0B69BA52E6D7DBAFA31;PSTM=1692628404;BAIDUID=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1;Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34=1704350597,1704352635;H_PS_PSSID=39998_40039;BDSFRCVID=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5;H_BDCLCKID_SF=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P;BDSFRCVID_BFESS=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5;H_BDCLCKID_SF_BFESS=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P;Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1704350597,1704352635,1705030651;Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1705030651;H_WISE_SIDS=39998_40039;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598;delPer=0;PSINO=2;BA_HECTOR=2g818h0h0k848501840l8h0hr06j5p1iq1g1m1t;ZFY=1QP1Ms5szl0UB:A70:ABLetAzVoqxEOfql5zZHKc1AGxY:C;BAIDUID_BFESS=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1;ZD_ENTRY=baidu;__bid_n=18a96e4c50a3728a150862;BDUSS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb;BDUSS_BFESS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb'
        # cookie = 'STOKEN=3e56105c148a5b8bba0b7743ac90d947ac164f12bd6f28cb1fb3852008722c72; TIEBA_USERTYPE=dc152df681623ffab2e16140; pplogid=5207YnIMd56jMpA3sBXjCuVyWkJubkLpLAUZLh3iGDfMmXWfp2AQ6lUg3K9HeNctKeD1WvoBvDnby15DUB%2BKauUjFW136hVTAQfi5yom%2BjaYGzLO7lyv3AG7Or5QEE8427my; BDUSS=9JYUszNGlxYVhHfnVtbzJwSDQxMThETW1nMU1aVFBhc2FDSnRVbERuQ2QxbE5sRVFBQUFBJCQAAAAAAQAAAAEAAACSsKCFxsHHtdnFxrDS1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ1JLGWdSSxlbW; PTOKEN=ec7c6d05c07b0015730a93addc34cd4c; PASSID=q3gk1Y; UBI=fi_PncwhpxZ%7ETaJc175MUrF-6-W-80wnspORD75-mo1TMvW8Kq7bZC6zDR2ZLBA3GDEj2isxJY9MCnaKMBNN5ay6NUu2KgAUzyFpMSCGIQZ8AocZBM9MHeYzrQ30Y%7ECBL4cZqK9QPINDn5EdgYwgtHnsPeFzQ__; BAIDUID=EBDC700FE54F863417712BB9BF97D909:FG=1'
        # cookie = 'STOKEN=3e56105c148a5b8bba0b7743ac90d947ac164f12bd6f28cb1fb3852008722c72; TIEBA_USERTYPE=dc152df681623ffab2e16140; pplogid=5207YnIMd56jMpA3sBXjCuVyWkJubkLpLAUZLh3iGDfMmXWfp2AQ6lUg3K9HeNctKeD1WvoBvDnby15DUB%2BKauUjFW136hVTAQfi5yom%2BjaYGzLO7lyv3AG7Or5QEE8427my; BDUSS=9JYUszNGlxYVhHfnVtbzJwSDQxMThETW1nMU1aVFBhc2FDSnRVbERuQ2QxbE5sRVFBQUFBJCQAAAAAAQAAAAEAAACSsKCFxsHHtdnFxrDS1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ1JLGWdSSxlbW; PTOKEN=ec7c6d05c07b0015730a93addc34cd4c; PASSID=q3gk1Y; UBI=fi_PncwhpxZ%7ETaJc175MUrF-6-W-80wnspORD75-mo1TMvW8Kq7bZC6zDR2ZLBA3GDEj2isxJY9MCnaKMBNN5ay6NUu2KgAUzyFpMSCGIQZ8AocZBM9MHeYzrQ30Y%7ECBL4cZqK9QPINDn5EdgYwgtHnsPeFzQ__; BAIDUID=EBDC700FE54F863417712BB9BF97D909:FG=1'
        # cookie = 'BIDUPSID=D5625B647EC9B0B69BA52E6D7DBAFA31; PSTM=1692628404; BAIDUID=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1; Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34=1704350597,1704352635; H_PS_PSSID=39998_40039; BDSFRCVID=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P; BDSFRCVID_BFESS=SZIOJeC62wN6ytQqwdeP-EsEh6CHRpnTH6aoheIEALVZ9RyVSqsVEG0PcU8g0KuMEAo6ogKKymOTHukF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbAfVCL5tI_3fP36q4oK5PLt-UQ0aPRX5-o2WDvRyqTcOR5Jj65bX6K-5bQD--3-LPj4Qh5SJqO1V4Jk3MA--t4Jbtr43x7pyJ5NXxQR-4O4sq0x0-ble-bQypou0xoyJDOMahvXal7xO-5cQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J5kqJJ7P; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1704350597,1704352635,1705030651; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1705030651; H_WISE_SIDS=39998_40039; delPer=0; PSINO=2; BA_HECTOR=2g818h0h0k848501840l8h0hr06j5p1iq1g1m1t; ZFY=1QP1Ms5szl0UB:A70:ABLetAzVoqxEOfql5zZHKc1AGxY:C; BAIDUID_BFESS=D5625B647EC9B0B6A1C4608507801E2B:SL=0:NR=10:FG=1; ZD_ENTRY=baidu; __bid_n=18a96e4c50a3728a150862; BDUSS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb; BDUSS_BFESS=XI3V1M2eW1td3NyZERPaUdrWjF5bTd-aWdYMllqRnVOYzQ0RGtXdXh0OGdrY2hsRVFBQUFBJCQAAAAAAQAAAAEAAACuBbw8Z2pqamI0MjEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAEoWUgBKFlb; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
        cookie = 'dfid=1txB9F00iUXy2XUUrv0kWHc3;UserName=kgopen1060636026;t=90fd7dd973f4120bc29213b95ed9d40b119ce46a925a2093b59a543bb1481730;kg_login=https://m.kugou.com/loginReg.php?act=login&url=https%3A%2F%2Factivity.kugou.com%2Fyk2024%2Fv-02e13a70%2Findex.html%3Fsource_id%3D532901;mid=337d2373829c8b7bae2ea114601372a0;ThirdData=partnerid=1&access_token=1B1D72C425104419158F7C6D65591A62&openid=551D766C33148062CDA9A8667EB7A659&nickname=%u0041%u0041%u0041%u0041%u738b%u5b50%u5c0f%u65b0&photo=http%3A%2F%2Fthirdqq.qlogo.cn%2Fek_qqapp%2FAQUtXDbPlzeZpicUC1RDictREFN4HqRgg31Lt2GIq2XMr7eNpuazvRN1UB8OgfLp779gBeias0r5AtkufG1OqqUNjMjl7icsrS42cazdRbOp35LccMxMEP4%2F100;KuGoo=KugooID=1060636026&KugooPwd=2BE2D7AF5D16FD821E88AF2140111308&NickName=%u006b%u006b%u0079%u0079%u0036&Pic=http://imge.kugou.com/kugouicon/165/20170510/20170510000348195256.jpg&RegState=1&RegFrom=QQ&t=90fd7dd973f4120bc29213b95ed9d40b119ce46a925a2093b59a543bb1481730&a_id=1058&ct=1706646244&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0031%u0030%u0036%u0030%u0036%u0033%u0036%u0030%u0032%u0036&t1=;kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e;kg_dfid=1txB9F00iUXy2XUUrv0kWHc3;KugooID=1060636026;a_id=1058;kg_mid=337d2373829c8b7bae2ea114601372a0;'
        d = self.parse_cookie(cookie)
        self.webview.page().profile().cookieStore().deleteAllCookies()
        for key, value in d.items():
            cookie_str = QNetworkCookie(QByteArray(key.encode()), QByteArray(value.encode()))
            cookie_str.setDomain('.kugou.com')
            print(cookie_str)
            self.webview.page().profile().cookieStore().setCookie(cookie_str)
        #
        # self.webview.page().profile().cookieStore().loadAllCookies()
        self.webview.load(url)

        # self.webview.page().profile().setPersistentCookiesPolicy(
        #     QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)
        self.webview.load(url)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "输入URL", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "加载", None, -1))
        self.pushButton1.setText(QtWidgets.QApplication.translate("MainWindow", "获取当前页地址", None, -1))
        self.pushButton2.setText(QtWidgets.QApplication.translate("MainWindow", "后退", None, -1))


from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
