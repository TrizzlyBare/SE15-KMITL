#No.1

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("KMITL Phone")

calculation = ""

def phone_num(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def clear_field():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def dial():
    messagebox.showinfo("Dialing", "Dailing " + calculation)

root.geometry("250x220")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=9)

btn_1 = tk.Button(root, text="1", command=lambda: phone_num(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=0, columnspan=2)
btn_2 = tk.Button(root, text="2", command=lambda: phone_num(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2, columnspan=2)
btn_3 = tk.Button(root, text="3", command=lambda: phone_num(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=4, columnspan=2)
btn_4 = tk.Button(root, text="4", command=lambda: phone_num(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=0, columnspan=2)
btn_5 = tk.Button(root, text="5", command=lambda: phone_num(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2, columnspan=2)
btn_6 = tk.Button(root, text="6", command=lambda: phone_num(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=4, columnspan=2)
btn_7 = tk.Button(root, text="7", command=lambda: phone_num(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=0, columnspan=2)
btn_8 = tk.Button(root, text="8", command=lambda: phone_num(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2, columnspan=2)
btn_9 = tk.Button(root, text="9", command=lambda: phone_num(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=4, columnspan=2)
btn_star = tk.Button(root, text="*", command=lambda: phone_num("*"), width=5, font=("Arial", 14))
btn_star.grid(row=5, column=0, columnspan=2)
btn_0 = tk.Button(root, text="0", command=lambda: phone_num(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2, columnspan=2)
btn_hash = tk.Button(root, text="#", command=lambda: phone_num("#"), width=5, font=("Arial", 14))
btn_hash.grid(row=5, column=4, columnspan=2)

btn_equal = tk.Button(root, text="Talk", command=dial, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=0, columnspan=3)

btn_clear = tk.Button(root, text="<", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=3, columnspan=3)
root.mainloop()

#=======================================================================================================

#No.2

import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=1, columnspan=2)

btn_clear = tk.Button(root, text="AC", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=3, columnspan=2)
root.mainloop()

#=======================================================================================================

#No.3

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
