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
