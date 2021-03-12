import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets


form_class = uic.loadUiType("myqt09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick)
        self.pb1_2.clicked.connect(self.myclick)
        self.pb1_3.clicked.connect(self.myclick)
        self.pb1_4.clicked.connect(self.myclick)
        self.pb1_5.clicked.connect(self.myclick)
        self.pb1_6.clicked.connect(self.myclick)
        self.pb1_7.clicked.connect(self.myclick)
        self.pb1_8.clicked.connect(self.myclick)
        self.pb1_9.clicked.connect(self.myclick)
        self.pb1_10.clicked.connect(self.myclick)
        self.pb1_11.clicked.connect(self.myCall)
        
    def myclick(self):
        txt_old = self.le.text()
        txt_new = self.sender().text()
        
        self.le.setText(txt_old+txt_new)
    
    def myCall(self):
        num = self.le.text()
        QtWidgets.QMessageBox.about(self, 'PhoneCall', "Calling...\n"+num)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()