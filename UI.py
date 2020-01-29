# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drawRectangle = QtWidgets.QPushButton(self.centralwidget)
        self.drawRectangle.setGeometry(QtCore.QRect(80, 80, 131, 51))
        self.drawRectangle.setObjectName("drawRectangle")
        self.drawLine = QtWidgets.QPushButton(self.centralwidget)
        self.drawLine.setGeometry(QtCore.QRect(80, 140, 131, 51))
        self.drawLine.setObjectName("drawLine")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 380, 131, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 210, 31, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 31, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 31, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 350, 31, 17))
        self.label_5.setObjectName("label_5")
        self.x1 = QtWidgets.QTextEdit(self.centralwidget)
        self.x1.setGeometry(QtCore.QRect(100, 200, 71, 31))
        self.x1.setObjectName("x1")
        self.y1 = QtWidgets.QTextEdit(self.centralwidget)
        self.y1.setGeometry(QtCore.QRect(100, 240, 71, 31))
        self.y1.setObjectName("y1")
        self.x2 = QtWidgets.QTextEdit(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(100, 300, 71, 31))
        self.x2.setObjectName("x2")
        self.y2 = QtWidgets.QTextEdit(self.centralwidget)
        self.y2.setGeometry(QtCore.QRect(100, 340, 71, 31))
        self.y2.setObjectName("y2")
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 50, 900, 538))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.drawRectangle.setText(_translate("MainWindow", "Draw Rectangle"))
        self.drawLine.setText(_translate("MainWindow", "Draw Line"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "X1:"))
        self.label_3.setText(_translate("MainWindow", "Y1:"))
        self.label_4.setText(_translate("MainWindow", "X2:"))
        self.label_5.setText(_translate("MainWindow", "Y2:"))

