import tkinter as tk

class App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("A simple paint program")
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=600, height=400, bg = "white")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button_clear = tk.Button(self, text="clear", command=self.clear_all)
        self.text = tk.Label(self, text="Drag the mouse to draw")
        self.text.pack(side="top")
        self.button_clear.pack(side="top")
        self.canvas.bind("<B1-Motion>", self.draw)

    def clear_all(self):
        self.canvas.delete("all")

    def draw(self, event):
        self.x = event.x
        self.y = event.y
        r=5
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill="black")

app = App()
app.mainloop()
