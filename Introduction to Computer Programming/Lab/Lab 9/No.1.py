from tkinter import *

class Counter:
    def __init__(self):
        window = Tk()
        window.title("Spinner")
        self.count = 0
        self.label = Label(window, text="0", font=("Helvetica", 30))
        self.label.grid(row=0, column=0)

        frame = Frame(window)
        frame.grid(row=0, column=2) 

        button1 = Button(frame, text="+", command=self.add)
        button2 = Button(frame, text="-", command=self.sub)
        button3 = Button(frame, text="Reset", command=self.reset)

        button1.grid(row=0, column=1)  
        button2.grid(row=1, column=1) 
        button3.grid(row=2, column=1)  

        window.mainloop()

    def add(self):
        self.count += 1
        self.label["text"] = str(self.count)

    def sub(self):
        self.count -= 1
        self.label["text"] = str(self.count)

    def reset(self):
        self.count = 0
        self.label["text"] = str(self.count)

Counter()