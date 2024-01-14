import pickle
import tkinter as tk
from tkinter import filedialog  

phonebook = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    phonebook[name] = number

def delete_contact():
    name = input("Enter name: ")
    if name in phonebook:
        del phonebook[name]
    else:
        print("Contact not found")

def find_contact():
    name = input("Enter name: ")
    try:
        if name in phonebook:
            print(name, ":", phonebook[name])
        else:
            raise Exception("Contact not found")
        
    except Exception as e:
        print(f"Error finding contact: {e}")

def save_all_contacts_to_file():
    root = tk.Tk()
    root.withdraw()
    file_name = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickled Files", ".pkl")])
    if not file_name:
        print("File not saved.")
        return

    try:
        with open(file_name, "wb") as fh:
            pickle.dump(phonebook, fh)
        print("Saved all contacts to file")
    except Exception as e:
        print(f"Error saving contacts to file: {e}")

def load_previous_contacts_from_file():
    root = tk.Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename(filetypes=[("Pickled Files", ".pkl")])
    if not file_name:
        print("File not loaded.")
        return

    try:
        with open(file_name, "rb") as fh:
            global phonebook
            phonebook = pickle.load(fh)
        print("Loaded all contacts from file")
    except Exception as e:
        print(f"Error loading contacts from file: {e}")

def print_all_contacts():
    for name, number in phonebook.items():
        print(name, ":", number)

def quit_phonebook():
    print("Goodbye")
    exit()

while True:
    print("+. Add contact")
    print("-. Delete contact")
    print("f. Find contact")
    print("s. Save all contacts to file")
    print("l. Load all contacts from file")
    print("p. Print all contacts")
    print("q. Quit")
    choice = input("Enter your choice: ")
    try:
        if choice == "+":
            add_contact()
        elif choice == "-":
            delete_contact()
        elif choice == "f":
            find_contact()
        elif choice == "s":
            save_all_contacts_to_file()
        elif choice == "l":
            load_previous_contacts_from_file()
        elif choice == "p":
            print_all_contacts()
        elif choice == "q":
            quit_phonebook()
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice")
