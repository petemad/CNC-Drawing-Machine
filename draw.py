import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QMessageBox
import serial
from time import sleep


class Draw(QtWidgets.QMainWindow):
    def __init__(self):
        super(Draw, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.label = QtGui.QPixmap()
        self.ui.drawRectangle.clicked.connect(self.draw_rectangle)
        self.ui.x1.textChanged.connect(self.read_x1)
        self.ui.x2.textChanged.connect(self.read_x2)
        self.ui.y1.textChanged.connect(self.read_y1)
        self.ui.y2.textChanged.connect(self.read_y2)
        self.ui.pushButton_3.clicked.connect(self.clear)
        self.ui.drawLine.clicked.connect(self.draw_line)

        self.x1 = 1
        self.x2 = 2
        self.y1 = 1
        self.y2 = 2
        self.location = [0,0]

    def read_x1(self):
        try :
            self.x1 = int(self.ui.x1.toPlainText())
            if self.x1 > 21 or self.x1 < 0 :
                self.error("A4 boundary error (21 x 29)")
                self.x1 = 1
                self.ui.x1.setText(None)
        except :
            self.x1 = 1
    
    def read_x2(self):
        try :
            self.x2 = int(self.ui.x2.toPlainText())
            if self.x2 > 21 or self.x2 < 0 :
                self.error("A4 boundary error (21 x 29)")
                self.x2 = 1
                self.ui.x2.setText(None)

        except :
            self.x2 = 2
    
    def read_y1(self):
        try :
            self.y1 = int(self.ui.y1.toPlainText())
            if self.y1 > 29 or self.y1 < 0 :
                self.error("A4 boundary error (21 x 29)")
                self.y1 = 1
                self.ui.y1.setText(None)
        except :
            self.y1 = 1
    
    def read_y2(self):
        try :
            self.y2 = int(self.ui.y2.toPlainText())
            if self.y2 > 29 or self.y2 < 0:
                self.error("A4 boundary error (21 x 29)")
                self.y2 = 2
                self.ui.y2.setText(None)
        except :
           self.y2 = 2

    def draw_rectangle(self):
        x = [self.x1,self.x2,self.x2,self.x1,self.x1]
        y = [self.y1,self.y1,self.y2,self.y2,self.y1]
        self.ui.graphicsView.plot(x,y,pen=pg.mkPen(color='r',width=2))
    
    def draw_line(self):
        x=[self.x1,self.x2]
        y=[self.y1,self.y2]
        self.ui.graphicsView.plot(x,y,pen=pg.mkPen(color='b',width=2))
    
    def clear(self):
        self.ui.graphicsView.clear()
        self.return_to_origin(self.location[0],self.location[1])

    def error(self, message):
        errorBox = QMessageBox()
        errorBox.setIcon(QMessageBox.Warning)
        errorBox.setWindowTitle('Error')
        errorBox.setText(message)
        errorBox.setStandardButtons(QMessageBox.Ok)
        errorBox.exec_()

    def go_from_origin(self,x,y):
        self.sendData("pf")
        sleep(0.5)
        if x[0] < x[1] :
            smallerX = x[0]
            useY = y[0]
        else :
            smallerX = x[1]
            useY = y[1]
        self.location = [smallerX,useY]
        self.sendData("mr"+str(smallerX))
        sleep(1.5)
        self.sendData("mu"+str(useY))
        sleep(1.5)

    def return_to_origin(self.x,y):
        self.sendData("pf")
        sleep(0.5)
        self.sendData("ml"+str(x))
        sleep(1.5)
        self.sendData("md"+str(y))
        self.location = [0,0]

    def go_right(self,length):
        self.sendData("mr"+str(length))
        sleep(1)
        self.location = self.location[0] + length
    def go_left(self,length):
        self.sendData("ml"+str(length))
        sleep(1)
        self.location = self.location[0] - length
    def go_up(self,length):
        self.sendData("mu"+str(length))
        sleep(1)
        self.location = self.location[1] + length
    def go_down(self,length):
        self.sendData("md"+str(length))
        self.location = self.location[1] - length
        sleep(1)

    def draw_rectangle_paper(self):
        if self.x1 < self.x2 :
            x = self.x1
            y = self.y1
        else :
            x= self.x2
            y = self.y2
        self.go_from_origin(x,y)
        self.go_right(np.aps(self.x1-self.x2))
        if x == self.x1 :
            if self.y1 < self.y2 :
                self.go_up(np.abs(self.y1 - self.y2))
                went = 'up'
            else :
                self.go_down(np.abs(self.y1 - self.y2))
                went = 'down'
        else :
            if self.y2 < self.y1 :
                self.go_up(np.abs(self.y1 - self.y2))
                went = 'up'
            else :
                self.go_down(np.abs(self.y1 - self.y2))
                went = 'down'
        self.go_left(np.aps(self.x1-self.x2))
        if went == 'up' :
            self.go_down(np.abs(self.y1 - self.y2))
        else :
            self.go_up(np.abs(self.y1 - self.y2))
        self.return_to_origin(self.location[0],self.location[1])
        
    def draw_line_paper(self,x,y):
        if location[0] == 0, location[1] == 0 :
            self.go_from_origin(x,y)
        self.sendData("pn")
        sleep(0.5)
        self.sendData("mr"+str(np.abs(x[1]-x[0])))
        self.location = [self.location[0] + np.abs(x[1]-x[0]),
                        self.location[1] + np.abs(y[1]-y[2])]
        sleep(0.1)
        self.sendData("mu"str(np.abs(y[1]-y[2])))        

    def sendData(self, char):
        try :
            s = serial.Serial('COM12',9600,timeout =1)
            data = bytearray(char , 'utf-8')
            s.write(data)
        except :
            sendData(char)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Draw()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()