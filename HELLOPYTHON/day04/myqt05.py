import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
import string

form_class = uic.loadUiType("myqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        hello = "\nhello"
        # obj = QTextEdit(self.te())
        # obj.text
        # TextEdit는 toplainText를 받으면서 감.
        hello1 = self.te.toPlainText()
            
        self.te.setText(hello1 + hello)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()