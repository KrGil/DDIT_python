import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from astropy.units import pb

form_class = uic.loadUiType("myqt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.arr2D=[
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
            ]
        self.arr2pb = []
        self.flag_wb = True
        
        for i in range(0, 10):
            line = []
            for j in range(0, 10):#(0,1)(0,2) i는 y축 j는 x축을 표한다.
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(40*j, 40*i, 40, 40))
                pb.clicked.connect(self.myclick) #evnet걸기 self는 적지 않는다.
                pb.setToolTip("{},{}".format(i, j))
                pb.setStatusTip("{},{}".format(i, j))
                line.append(pb)
            self.arr2pb.append(line)
        self.myrender()
        
    def myrender(self): #rendering 부터 그 다음 event를 작성한다.
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('1.png'))
                else :
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('2.png'))
                    
    def myclick(self) :
        str = self.sender().toolTip()
        arr = str.split(",")
        i =  int(arr[0])
        j = int(arr[1])     
        
        if self.arr2D[i][j] != 0 :
            return 
        
        int_wb = 0
        if self.flag_wb :
            self.arr2D[i][j] = 1
            int_wb = 1
        else :
            self.arr2D[i][j] = 2
            int_wb = 2
        
        self.myrender()
        up = self.getUp(i, j, int_wb)
        dw = self.getDW(i, j, int_wb)
        ri = self.getRi(i, j, int_wb)
        le = self.getLe(i, j, int_wb)
        ur = self.getUR(i, j, int_wb)
        dl = self.getDL(i, j, int_wb)
        dr = self.getDR(i, j, int_wb)
        ul = self.getUL(i, j, int_wb)
        if up+dw >= 4 or ri+le >=4 or ur+dl >=4 or dr +ul >=4:
            QtWidgets.QMessageBox.about(self, '결과', "Victory\n"+self.result(self, int_wb))
        
        self.flag_wb = not self.flag_wb # boolean 바꿔주는 명령어.
    
    def getUp(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                i -= 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt >= 5 :
                       
                        return str
                else :
                    return cnt
        except :
            return cnt
    def getDW(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                i += 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
        
    def getRi(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                j += 1
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
    def getLe(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                j -= 1
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
    
    def getUR(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                j += 1
                i -= 1
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
    def getDL(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                j -= 1
                i += 1
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
            
    def getDR(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                j += 1
                i += 1
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
    def getUL(self, i, j, int_wb):
        cnt = 0
        try :
            while True :
                j -= 1
                i -= 1
                if i < 0 or j < 0:
                    return cnt
                if self.arr2D[i][j] == int_wb :
                    cnt += 1
                    if cnt > 5 :
                        self.result(self, i, j, int_wb)
                else :
                    return cnt
        except :
            return cnt
            
    def result(self, int_wb):
        wb= ""
        if int_wb == 1:
            wb = "흰돌"
        else :
            wb = "검은돌"
        return wb
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()