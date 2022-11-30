# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from screeninfo import get_monitors

dir = os.getcwd().replace('\\','/')

lnks, icons = [],[]

positions = []

def load():
    global lnks, icons
    lnks, icons = [],[]

    with open('applist.txt','r') as f:
        t = f.readlines()
    for i in range(len(t)):
        s = t[i].strip().split('||')
        lnks.append(s[0])
        icons.append(s[1])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global positions
        positions = []
        MainWindow.setObjectName("MainWindow")
        for m in get_monitors():
            positions.append([m.x,m.y,m.width,m.height])

        
        MainWindow.setWindowOpacity(1.0)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)# if self.on_top else QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowFlags(flags)
        MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.buttons = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xy = [0,0]

        MainWindow.setCentralWidget(self.centralwidget)
        self.btnrenderer(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.show() #나중에 그걸로 바꿀것. 마우스가 화면아래로 오는지 감지해서 하는 그거

    def btnrenderer(self, MainWindow):
        load()
        MainWindow.resize(len(lnks)*70, 70)
        for i in range(len(lnks)):
            b = 0
            b = QtWidgets.QPushButton(self.centralwidget)
            b.setGeometry(QtCore.QRect(i*70, 0, 71, 71))
            b.setObjectName("pushButton_"+str(i)) if i!=0 else b.setObjectName("pushButton")
            b.setFlat(True)
            b.setStyleSheet("background-color: rgba(255, 255, 255, 0);background-image : url(%s);"%(dir+'/'+icons[i]))
            self.buttons.append(b)
        for i in range(len(lnks)):
            try:
                eval('self.buttons[%d].clicked.connect(lambda:os.startfile(dir+"/"+lnks[%d]))'%(i,i))
            except:
                pass # "아님 말고"ㅋㅋ



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
