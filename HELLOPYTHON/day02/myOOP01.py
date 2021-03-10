class Animal:
    def __init__(self): #생성자에게 전역변수를 해주어야만 한다.
        self.age = 1
        print("생성자")

    def __del__(self):
        print("소멸자")    
        
    def getOlder(self):
        self.age += 1

class Human(Animal):
    def __init__(self):
        super().__init__() #조상을 불러와야지 밑에서 실행할 수 있다. 자바와 달리 자동으로 불러오지 않는다.
        self.flag_coding = True
    
    def cutHand(self):
        self.flag_coding = False
    
    
if __name__ == "__main__":
    hum = Human()
    print(hum.age)
    print(hum.flag_coding)
    hum.cutHand()
    print(hum.age)
    print(hum.flag_coding)

