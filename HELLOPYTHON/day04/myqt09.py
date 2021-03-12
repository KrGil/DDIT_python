import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string
import random
from turtledemo.nim import computerzug
from sqlalchemy.inspection import _self_inspects

form_class = uic.loadUiType("myqt09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick_1)
        self.pb1_2.clicked.connect(self.myclick_2)
        self.pb1_3.clicked.connect(self.myclick_3)
        self.pb1_4.clicked.connect(self.myclick_4)
        self.pb1_5.clicked.connect(self.myclick_5)
        self.pb1_6.clicked.connect(self.myclick_6)
        self.pb1_7.clicked.connect(self.myclick_7)
        self.pb1_8.clicked.connect(self.myclick_8)
        self.pb1_9.clicked.connect(self.myclick_9)
        self.pb1_10.clicked.connect(self.myclick_0)
        self.pb1_11.clicked.connect(self.myclick_call)
   
    # def test(self):
        # test1 = self.QPushButton.text()
        # print(test1)
    def myclick_1(self):
        num = self.pb1.text()
        # obj = QLineEdit(self.le())
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_2(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_3(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_4(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_5(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_6(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_7(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_8(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_9(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_0(self):
        num = self.pb1.text()
        result = self.le.text()
        
        self.le.setText(result + num)
    def myclick_call(self):
        result_num = self.le.text()
        
        QMessageBox.about(QWidget(), 'PhoneCall', "Calling...\n"+result_num)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()