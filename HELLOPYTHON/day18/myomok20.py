import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from astropy.units import fl
import numpy as np
from tensorflow.keras.models import load_model

form_class = uic.loadUiType("myomok20.ui")[0]
model = load_model('20201213_202430.h5')
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbreset.clicked.connect(self.myreset)
        self.arr_ij=[
                [0,0],
                [0,1],
                [0,2],
                [0,3],
                [0,4]
                ]
        self.seq = 0
        
        self.arr2D= np.zeros((20,20))
        self.arr2pb = []
        self.flag_wb = True
        self.flag_ing = True

        
        for i in range(20):
            line = []
            for j in range(20):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(40*j , 40*i, 40, 40))
                pb.clicked.connect(self.myclick)
                pb.setToolTip("{},{}".format(i,j))
                line.append(pb)
            self.arr2pb.append(line)
        
        self.myrender()
        
    def myreset(self):
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0

        self.flag_wb = True
        self.flag_ing = True  
        self.seq = 0
        self.myrender()
        
        
    def myclick(self):
        if not self.flag_ing:
            return
        
        str = self.sender().toolTip()
        arr = str.split(",")
        i = int(arr[0])
        j = int(arr[1])
        
        if self.arr2D[i][j] > 0:
            return
        int_wb = 0
        if self.flag_wb :   
            self.arr2D[i][j] = 1
            int_wb = 1
        else :
            self.arr2D[i][j] = 2  
            int_wb = 2
        self.myrender()
        
        up = self.getUP(i,j,int_wb)
        dw = self.getDW(i,j,int_wb)
        ri = self.getRI(i,j,int_wb)
        le = self.getLE(i,j,int_wb)
        
        ul = self.getUL(i,j,int_wb)
        ur = self.getUR(i,j,int_wb)
        dl = self.getDL(i,j,int_wb)
        dr = self.getDR(i,j,int_wb)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self, "omok", "백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self, "omok", "흑돌이 이겼습니다.")
            self.flag_ing = False    
            return
        
        self.flag_wb = not self.flag_wb
        
        input = self.arr2D.copy()
        input[(input != 1) & (input != 0)] = -1
        input[(input == 1) & (input != 0)] = 1
        input = np.expand_dims(input, axis=(0, -1)).astype(np.float32)

        output = model.predict(input).squeeze()
        output = output.reshape((20, 20))
        output_x, output_y = np.unravel_index(np.argmax(output), output.shape)
            
        print("error")
        int_wb = 0
        if self.flag_wb :
            print("error1")   
            self.arr2D[output_x][output_y] = 1
            int_wb = 1
        else :
            print("error2")   
            self.arr2D[output_x][output_y] = 2  
            int_wb = 2
            print("error2")
            
        self.comrender(output_x, output_y)
        print("error3")   
        
        up = self.getUP(output_x,output_y,int_wb)
        dw = self.getDW(output_x,output_y,int_wb)
        ri = self.getRI(output_x,output_y,int_wb)
        le = self.getLE(output_x,output_y,int_wb)
        
        ul = self.getUL(output_x,output_y,int_wb)
        ur = self.getUR(output_x,output_y,int_wb)
        dl = self.getDL(output_x,output_y,int_wb)
        dr = self.getDR(output_x,output_y,int_wb)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            QtWidgets.QMessageBox.about(self, "omok", "백돌이 이겼습니다." if self.flag_wb else "흑돌이 이겼습니다.")
            self.flag_ing = False
        
        self.flag_wb = not self.flag_wb
        
        
    def getDR(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                i += 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDL(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                i += 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUR(self,i,j,int_wb):    
        cnt = 0
        while True :
            i -= 1
            j += 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt 
            if self.arr2D[i][j] == int_wb:
                cnt += 1
            else:
                return cnt
        
        
    def getUL(self,i,j,int_wb):    
        cnt = 0
        while True :
            i -= 1
            j -= 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt 
            if self.arr2D[i][j] == int_wb:
                cnt += 1
            else:
                return cnt
        
        
    def getLE(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt        
        
    def getRI(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt        
        
        
    def getDW(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    
    def getUP(self,i,j,int_wb):    
        cnt = 0
        while True :
            i -= 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt
            if self.arr2D[i][j] == int_wb:
                cnt += 1
            else:
                return cnt
        
        
    def myrender(self):
        print("error4")
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('2.png'))
    def comrender(self, output_x, output_y):
        print("error5")
        for i in range(20):
            for j in range(20):
                if self.arr2D[output_x][output_y] == 0:
                    self.arr2pb[output_x][output_y].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[output_x][output_y] == 1:
                    self.arr2pb[output_x][output_y].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[output_x][output_y] == 2:
                    self.arr2pb[output_x][output_y].setIcon(QtGui.QIcon('2.png'))
               
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    