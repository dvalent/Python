

cols = 50 # multiple of size!
row  = 50
openSet = []
closeSet = []
myArray = []
width = 500
height = 500
w = width / cols
h = height / row

class spot:
    def __init__(self,col):
        self.col = 255,0,255
        
        self.f = 0
        self.g = 0
        self.h = 0

    def show(self,i,j):
        ellipseMode(CORNER)
        stroke(0,0,0)
        fill(col)
        #noFill()
        ellipse(i,j, w, h)

        
    

    
def setup():
    size(height,width)
    smooth()

    
    
def draw():
    background(51)
        
    for i in range(0,width , width / cols):
        myArray_cols = []
        for j in range(0,height, height / row):
            myobject = spot(255)
            myobject.show(i,j)
            myArray_cols.append((i,j))
        myArray.append(myArray_cols)
        
    start = myArray[0][0]
    end = myArray[(height / row)-1][(height / row)-1]
    
    openSet.append(start)
    
    print len(openSet)
    for i in openSet:
        openObj = spot()
        openObj.show(i[0],i[1])


            