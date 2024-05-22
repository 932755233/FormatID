# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qiangshagnchenguizNvuEA.ui'
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
        MainWindow.resize(453, 340)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 160, 211, 41))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(120, 80, 181, 20))
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.le_right_time = QLineEdit(self.splitter)
        self.le_right_time.setObjectName(u"le_right_time")
        self.splitter.addWidget(self.le_right_time)
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(120, 120, 187, 20))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.le_y_time = QLineEdit(self.splitter_2)
        self.le_y_time.setObjectName(u"le_y_time")
        self.splitter_2.addWidget(self.le_y_time)
        self.cb_status = QCheckBox(self.centralwidget)
        self.cb_status.setObjectName(u"cb_status")
        self.cb_status.setGeometry(QRect(180, 30, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 453, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf\u5355\u4f4d\uff1a\u6beb\u79d2\u3002\u5f00\u5173\uff1aCTRL+F6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9f20\u6807\u53f3\u952e\u5ef6\u8fdf", None))
        self.le_right_time.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y\u952e\u5ef6\u8fdf", None))
        self.le_y_time.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.cb_status.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u5173\u95ed", None))
    # retranslateUi

