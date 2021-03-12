import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string

form_class = uic.loadUiType("myqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        dan = self.le.text()
        dan_int = int(dan)
        result = ""
        for i in range(dan_int, 10):
            result += str(dan_int)+" * "+ str(i) +" = " + str(dan_int * i) + "\n"
            
        self.te.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()