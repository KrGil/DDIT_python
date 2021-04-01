
def changeValue(a):
    a =  5

def changeRef(a):
    a[0] = 5
    
if __name__ == '__main__':
    a = 0
    arr = [0]
    
    print(a)
    print(arr)
    
    changeValue(a)
    changeRef(arr)
    
    print(a)
    print(arr)