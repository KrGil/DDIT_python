import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string

form_class = uic.loadUiType("myqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        obj = QLineEdit(self.le1)
        # 메서드 종류를 모를 때 obj로 그 객체를 받아와서 ctrl+space로 찍어보자
        obj.setText()
        
        num1 = self.le1.text()
        num2 = self.le2.text()
        
        result = 0
        for i in range(int(num1), int(num2)+1):
            result += i
            
        self.le3.setText(str(result))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()