import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from astropy.units import pb

form_class = uic.loadUiType("myqt01_fiveEyes19.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_reset.clicked.connect(self.resetButton)
        self.arr2D=[
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            ]
        self.arr2pb = []
        self.flag_wb = True
        self.flag_ing = True
        
        for i in range(0, 19):
            line = []
            for j in range(0, 19):#(0,1)(0,2) i는 y축 j는 x축을 표한다.
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
        
    def resetButton(self):
        # 배열은 주소 
        for i in range(0, 19):
            for j in range(0, 19):
                self.arr2D[i][j]=0
                
        self.flag_ing = True
        self.flag_wb = True
        self.myrender()
        
    def myrender(self): #rendering 부터 그 다음 event를 작성한다.
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('1.png'))
                else :
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('2.png'))
                    
    def myclick(self) :
        if not self.flag_ing :
            return 
        
        if self.flag_wb:
            self.pb_turn.setIcon(QtGui.QIcon('2.png'))
        else :
            self.pb_turn.setIcon(QtGui.QIcon('1.png'))
            
            
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
        
        # 섬세한 디테일을 적용시키자!
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = dr + ul + 1
        
        if d1 >= 5 or d2 >= 5 or d3 >= 5 or d4 >= 5:
            QtWidgets.QMessageBox.about(self, '결과', "Victory\n"+self.result(int_wb))
            self.flag_ing = not self.flag_ing
        
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