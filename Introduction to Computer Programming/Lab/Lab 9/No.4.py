from tkinter import *
from tkinter import messagebox
import random

class App:
    def __init__(self):
        window = Tk()
        window.title("Draw Circle")

        self.canvas = Canvas(window, width=700, height=400, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.canvas.create_rectangle(50, 50, 350, 200)

        self.canvas.bind("<Button-1>", self.drawCircle)

        window.mainloop()

    def warning(self):

        messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")

    def drawCircle(self, event):
        if event.x >= 50 and event.x <= 350 and event.y >= 50 and event.y <= 200:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="#%02x%02x%02x" % (r, g, b))
        else:
            self.warning()
    
App()