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
		self.mainloop()
	
	def drawGrid(self):
		for i in range(0,901,50):
				self.theCanvas.create_line(i+self.offset,0+self.offset,i+self.offset,900+self.offset,fill="grey")
				self.theCanvas.create_line(0+self.offset,i+self.offset,900+self.offset,i+self.offset,fill="grey")
		self.theCanvas.create_rectangle(950,self.offset,1050,900+self.offset,fill="grey")
window = App()

