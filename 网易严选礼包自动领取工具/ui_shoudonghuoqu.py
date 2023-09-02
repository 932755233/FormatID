# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shoudonghuoqu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(966, 926)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ptePhoneList = QPlainTextEdit(self.centralwidget)
        self.ptePhoneList.setObjectName(u"ptePhoneList")
        self.ptePhoneList.setGeometry(QRect(10, 30, 351, 391))
        self.teResult = QTextEdit(self.centralwidget)
        self.teResult.setObjectName(u"teResult")
        self.teResult.setGeometry(QRect(10, 460, 351, 411))
        self.teResult.setReadOnly(True)
        self.pteTokenList = QPlainTextEdit(self.centralwidget)
        self.pteTokenList.setObjectName(u"pteTokenList")
        self.pteTokenList.setGeometry(QRect(380, 30, 351, 391))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 241, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 0, 241, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 430, 181, 16))
        self.pbStartGetCode = QPushButton(self.centralwidget)
        self.pbStartGetCode.setObjectName(u"pbStartGetCode")
        self.pbStartGetCode.setGeometry(QRect(770, 50, 161, 151))
        self.cbWithPhone = QCheckBox(self.centralwidget)
        self.cbWithPhone.setObjectName(u"cbWithPhone")
        self.cbWithPhone.setGeometry(QRect(810, 220, 101, 31))
        self.teOther = QTextEdit(self.centralwidget)
        self.teOther.setObjectName(u"teOther")
        self.teOther.setGeometry(QRect(380, 460, 570, 411))
        self.teOther.setReadOnly(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 430, 181, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.teResult.raise_()
        self.label.raise_()
        self.ptePhoneList.raise_()
        self.label_2.raise_()
        self.pteTokenList.raise_()
        self.label_3.raise_()
        self.pbStartGetCode.raise_()
        self.cbWithPhone.raise_()
        self.teOther.raise_()
        self.label_4.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 966, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9a8c\u8bc1\u7801\u5de5\u5177", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u624b\u673a\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165Token", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u65b9\u751f\u6210\u9a8c\u8bc1\u7801", None))
        self.pbStartGetCode.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.cbWithPhone.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u4e0a\u624b\u673a\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u4fe1\u606f", None))
    # retranslateUi