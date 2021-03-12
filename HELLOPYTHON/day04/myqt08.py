import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string
import random
from turtledemo.nim import computerzug
from sqlalchemy.inspection import _self_inspects

form_class = uic.loadUiType("myqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick_s)
        self.pb2.clicked.connect(self.myclick_r)
        self.pb2.clicked.connect(self.myclick_p)
        
    def myclick_s(self):
        # obj = QPushButton(self.pb1())
        
        me = self.pb1.text()
        self.lbl2.setText(me)
        
        com = self.computer()
        self.lbl4.setText(com)
        
        result = self.result(me,com)
        self.lbl6.setText(result)
        
    def myclick_r(self):
        me = self.pb2.text()
        self.lbl2.setText(me)
        
        com = self.computer()
        self.lbl4.setText(com)
        
        result = self.result(me,com)
        self.lbl6.setText(result)
        
    def myclick_p(self):
        me = self.pb3.text()
        self.lbl2.setText(me)
        
        com = self.computer()
        self.lbl4.setText(com)
        
        result = self.result(me,com)
        self.lbl6.setText(result)    
           
    def computer(self):
        rnd = random.random()
        com = ""
        if rnd > 0.7 :
            com = "가위"
        elif rnd > 0.4 :
            com = "바위"
        else :
            com = "보"
        return com    
    
    def result(self, a, b):
        result = ""
        if a == b :
            result = "비겼다"
        elif (a =="가위" and b == "바위") or (a=="바위" and b == "보") or (a=="보" and b == "가위") :
            result = "졌다"
        else :
            result = "이겼다"
        
        return result
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()