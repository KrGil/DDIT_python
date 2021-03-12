import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string
import random
from turtledemo.nim import computerzug

form_class = uic.loadUiType("myqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick_hol)
        self.pb2.clicked.connect(self.myclick_zzack)
        
    def myclick_hol(self):
        # obj = QPushButton(self.pb1())
        
        me = self.pb1.text()
        self.lbl2.setText(me)
        
        com = self.computer()
        self.lbl4.setText(com)
        
        result = self.result(me,com)
        self.lbl6.setText(result)
        
    def myclick_zzack(self):
        me = self.pb2.text()
        self.lbl2.setText(me)
        
        com = self.computer()
        self.lbl4.setText(com)
        
        result = self.result(me,com)
        self.lbl6.setText(result)
        
        
    def computer(self):
        rnd = random.random()
        com = ""
        if rnd < 0.5 :
            com = "홀"
        else :
            com = "짝"
        return com    
    
    def result(self, a, b):
        result = ""
        if a == b :
            result = "같다."
        else :
            result = "다르다."
        
        return result
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()