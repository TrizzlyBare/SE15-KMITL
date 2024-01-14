from tkinter import *
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self):
        self.window = Tk()
        self.window.title("Currency Converter")
        self.window.geometry("400x200")
        self.txt = IntVar() 

        Entry(self.window, textvariable=self.txt).pack()

        Button(self.window, text="USD -> THB", command=self.convert_to_thb).pack()
        Button(self.window, text="THB -> USD", command=self.convert_to_usd).pack()
        self.window.mainloop()
        
    def convert_to_thb(self):
        usd_amount = int(self.txt.get())
        thai_baht = usd_amount * 30.0
        messagebox.showinfo("Result", f"{usd_amount}USD = {thai_baht:.2f}THB")
        self.window.mainloop()
    
    def convert_to_usd(self):
        thai_baht = int(self.txt.get())
        usd_amount = thai_baht / 30.0
        messagebox.showinfo("Result", f"{thai_baht}THB = {usd_amount:.2f}USD")
        self.window.mainloop()
        
CurrencyConverter()
        