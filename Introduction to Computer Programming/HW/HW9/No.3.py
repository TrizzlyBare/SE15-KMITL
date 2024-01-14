from tkinter import *

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title("Mouse Events")
        self.width = 500
        self.height = 500
        self.canvas = Canvas(window, bg="white", width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.processLeftClick)
        self.canvas.bind("<Button-2>", self.processRightClick)
        self.ovals = [] 
        window.mainloop()

    def processLeftClick(self, event):
        oval = self.canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, tags="oval")
        self.ovals.append(oval) 

    def processRightClick(self, event):
        for oval in self.ovals:
            x1, y1, x2, y2 = self.canvas.coords(oval)
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.canvas.delete(oval)
                self.ovals.remove(oval)
                break

MainGUI()
