import random
import tkinter as tk
from tkinter import font as tkFont

class Level():
    def __init__(self, levelID):
        self.levelID = levelID
        self.objects=[]
        self.layout = [[None for col in range(18)] for row in range(18)]
        for i in range(10):
            x = random.randint(0,17)
            y = random.randint(0,17)
            while self.layout[y][x] is not None:
                x = random.randint(0,17)
                y = random.randint(0,17)
            self.layout[y][x] = Mirror(x,y,random.choice([0,1]),False)  # type: ignore
            self.objects.append(self.layout[y][x])
        self.laser = Laser(0,1,"red")
        self.objects.append(self.laser)


    def draw(self,theCanvas,offset):
        for object in self.objects:
            object.draw(theCanvas, offset)


class Mirror():
    def __init__(self,x,y,orientation, movable):
        self.x = x
        self.y = y
        self.orientation = orientation
        images = ["mirror1.png", "mirror2.png"]
        self.image = tk.PhotoImage(file=images[orientation])
        self.movable = movable

    def draw(self, canvas,offset):
        self.canvasID = canvas.create_image(offset+self.x*50, offset+self.y*50, image=self.image, anchor="nw")
        
class Laser():
    def __init__(self,x,y,colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.image = tk.PhotoImage(file="laser1.png")

    def draw(self,canvas,offset):
        self.canvasID = canvas.create_image(self.x*50+offset, self.y*50+offset,image=self.image, anchor="nw")

    def shoot(self, canvas, offset):
        currentx = self.x
        currenty = self.y
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        currentdir = 0
        while True:
            currentx += dirs[currentdir][1]
            currenty += dirs[currentdir][0]
            if 0<=currentx <=17 and 0<=currenty <=17:
                # on the board
                if currentdir == 0 or currentdir == 2:
                    canvas.create_line(currentx*50+offset,currenty*50+offset+25,(currentx+1)*50+offset, currenty*50+offset+25, fill="red")
                else:
                    canvas.create_line(currentx*50+offset+25,currenty*50+offset,(currentx+1)*50+offset+25, currenty*50+offset, fill="red")
            else:
                break

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1200x1000")
        self.theCanvas = tk.Canvas(self, width=1200, height=1000, bg="lightblue")
        self.theCanvas.grid(row=0, column=0)
        self.mirrors = []
        self.offset = 20
        self.drawGrid()
        l1 = Level(1)
        l1.draw(self.theCanvas,self.offset)
        self.theCanvas.bind("<B1-Motion>",self.drag)
        self.theCanvas.bind("<ButtonRelease-1>",self.dropped)
        self.theCanvas.bind("<Button-1>",self.clicked) 
self.mainloop()
    
    def drawGrid(self):
        for i in range(0,901,50):
            self.theCanvas.create_line(i+self.offset,0+self.offset,i+self.offset,900+self.offset,fill="grey")
            self.theCanvas.create_line(0+self.offset,i+self.offset,900+self.offset,i+self.offset,fill="grey")
        self.theCanvas.create_rectangle(950,self.offset,1050,900+self.offset,fill="grey")

    def drag(self,e):
        mouseX = e.x
        mouseY = e.y
        # get ID of nearest object
        IDNum = self.theCanvas.find_closest(mouseX, mouseY)[0]
        self.theCanvas.tag_raise(IDNum)
        self.jeffs[IDNum].drag(self.theCanvas, mouseX,mouseY)
    
    def dropped(self,e):
        pass
    
    def clicked(self,e):
        pass



window = App()



