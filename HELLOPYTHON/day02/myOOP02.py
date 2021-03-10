from Cython.Compiler.Naming import self_cname
class Dog:
    def __init__(self):
        self.flag_bark = True
    
    def cutSungdae(self):
        self.flag_bark = False
        
class Bird:
    def __init__(self):
        self.idx_fly = 0
    
    def training(self):
        self.idx_fly += 1
    
    def training_hard(self, power): #클래스 내의 메서드는 self는 항상 붙는다.
        self.idx_fly += power
        
class GaeSae(Dog, Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
        self.flag_kill = True
        
    def useKill(self):
        self.flag_kill = False
    
if __name__ == '__main__':
    gs = GaeSae()
    print(gs.flag_bark)
    print(gs.idx_fly)
    print(gs.flag_kill)
    
    gs.cutSungdae()
    gs.training_hard(5)
    gs.useKill()
    
    print(gs.flag_bark)
    print(gs.idx_fly)
    print(gs.flag_kill)
    
    
    