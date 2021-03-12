import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string

form_class = uic.loadUiType("myqt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        num1 = self.le1.text()
        num2 = self.le2.text()
        cal = self.lbl.text()
        
        if(cal == "+") :
            result_pre = int(num1) + int(num2)
            print(result_pre)
            
        self.le3.setText(str(result_pre))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()