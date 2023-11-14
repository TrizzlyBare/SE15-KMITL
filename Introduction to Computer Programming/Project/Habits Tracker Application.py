import tkinter as tk
from tkinter import simpledialog, messagebox, IntVar, ttk
import pickle
import os


class BasePage:
    def __init__(self, root, title, geometry):
        self.root = root
        self.title = title
        self.geometry = geometry
        self.setup_base_page()

    def setup_base_page(self):
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.root.resizable(False, False)

    def destroy(self):
        self.root.destroy()


class ProfileSelectionPage:
    def __init__(self, root):
        self.root = root
        self.profiles = []
        self.setup_profile_selection_page()
        self.load_profiles()
        self.create_profile_buttons()

    def setup_profile_selection_page(self):
        self.root.title("Profile Selection")
        self.root.geometry("400x700")
        self.root.resizable(False, False)

        self.select_profile_label = tk.Label(
            self.root,
            text="Select a Profile",
            font=("Arial", 20, "bold"),
            background="white",
            width=30,
            height=2,
        )
        self.select_profile_label.place(relx=0.5, rely=0.04, anchor=tk.CENTER)

        self.btn_new = tk.Button(self.root, text="+", width=4, command=self.new_profile)
        self.btn_new.place(x=320, y=660)

    def load_profiles(self):
        try:
            with open("profiles.pkl", "rb") as file:
                self.profiles = pickle.load(file)
        except FileNotFoundError:
            self.profiles = []

    def save_profiles(self):
        with open("profiles.pkl", "wb") as file:
            pickle.dump(self.profiles, file)

    def new_profile(self):
        if len(self.profiles) >= 10:
            messagebox.showinfo("Error", "You can only have up to 10 profiles.")
            return

        profile_name = simpledialog.askstring("New Profile", "Enter Profile Name:")
        if not profile_name:
            profile_name = f"Profile {len(self.profiles) + 1}"

        self.profiles.append(profile_name)
        self.save_profiles()
        self.refresh_buttons()

    def create_profile_buttons(self):
        profile_frame = tk.Frame(self.root)
        profile_frame.pack(pady=20)

        for i, profile_name in enumerate(self.profiles):
            self.create_profile_button(profile_frame, i, profile_name)

        profile_frame.place(relx=0.04, rely=0.1)

    def create_profile_button(self, frame, index, profile_name):
        profile_row = tk.Frame(frame)
        profile_row.pack()

        profile_btn = tk.Button(
            profile_row,
            text=f"  {profile_name}",
            width=38,
            height=2,
            font=("Arial", 12),
            command=lambda i=index: self.show_profile_page(self.profiles[i]),
        )
        profile_btn.pack(side=tk.LEFT)

        delete_btn = tk.Button(
            profile_row,
            text="🗑️",
            width=5,
            height=2,
            font=("Arial", 12),
            command=lambda i=index: self.delete_profile(i),
        )
        delete_btn.pack(side=tk.LEFT)

    def refresh_buttons(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_profile_selection_page()
        self.create_profile_buttons()

    def delete_profile(self, index):
        if 0 <= index < len(self.profiles):
            profile_name = self.profiles[index]
            habits_file = f"{profile_name}_habits.pkl"

            if os.path.exists(habits_file):
                os.remove(habits_file)

            del self.profiles[index]
            self.save_profiles()
            self.refresh_buttons()

    def show_profile_page(self, profile_name):
        profile_page_root = tk.Toplevel(self.root)
        self.root.withdraw()
        profile_page = ProfilePage(profile_page_root, profile_name)
        profile_page_root.wait_window()
        self.root.deiconify()


class ProfilePage:
    def __init__(self, root, profile_name):
        self.root = root
        self.profile_name = profile_name
        self.habits = self.load_habits()
        self.setup_profile_page()

    def setup_profile_page(self):
        self.root.title(f"{self.profile_name}")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.label = tk.Label(
            self.root,
            text=f"Profile: {self.profile_name}",
            font=("Arial", 20, "bold"),
            background="white",
            width=55,
            height=2,
        )
        self.label.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

        self.btn_return = tk.Button(
            self.root, text="⏎", width=5, command=self.return_to_profile_selection
        )
        self.btn_return.place(x=600, y=350)

        self.btn_add_habits = tk.Button(
            self.root, text="Add Habits", width=15, command=self.add_habits
        )
        self.btn_add_habits.place(relx=0.5, y=350, anchor=tk.CENTER)

        # Display habits using buttons
        self.display_habits()

    def return_to_profile_selection(self):
        self.save_habits()
        self.root.destroy()

    def add_habits(self):
        add_habits_root = tk.Toplevel(self.root)
        add_habits = AddHabitsPage(add_habits_root, self.profile_name, self)
        add_habits_root.wait_window()

    def display_habits(self):
        wanted_label = tk.Label(
            self.root, text="Wanted Habits:", font=("Arial", 14, "bold")
        )
        wanted_label.place(x=50, y=100)

        unwanted_label = tk.Label(
            self.root, text="Unwanted Habits:", font=("Arial", 14, "bold")
        )
        unwanted_label.place(relx=0.6, y=100)

        wanted_habits = [
            habit for habit in self.habits if not habit.endswith("(Unwanted)")
        ]
        unwanted_habits = [
            habit[:-11] for habit in self.habits if habit.endswith("(Unwanted)")
        ]

        for i, habit in enumerate(wanted_habits):
            habit_btn = tk.Button(
                self.root,
                text=f"{i + 1}. {habit}",
                font=("Arial", 12),
                command=lambda h=habit: self.handle_habit_button(h),
            )
            habit_btn.place(x=100, y=140 + i * 30)

        for i, habit in enumerate(unwanted_habits):
            habit_btn = tk.Button(
                self.root,
                text=f"{i + 1}. {habit}",
                font=("Arial", 12),
                command=lambda h=habit: self.handle_habit_button(h),
            )
            habit_btn.place(
                relx=0.55, x=100, y=140 + i * 30
            )  # Adjust the x parameter for the right side

    def handle_habit_button(self, habit):
        # You can implement any behavior you want when a habit button is clicked
        messagebox.showinfo("Habit Clicked", f"You clicked habit: {habit}")

    def load_habits(self):
        try:
            with open(f"{self.profile_name}_habits.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def save_habits(self):
        with open(f"{self.profile_name}_habits.pkl", "wb") as file:
            pickle.dump(self.habits, file)

class AddHabitsPage(BasePage):
    def __init__(self, root, profile_name, profile_page):
        super().__init__(root, "Add Habits", "700x400")
        self.profile_name = profile_name
        self.profile_page = profile_page
        self.setup_add_habits_page()

    def setup_add_habits_page(self):
        self.label = tk.Label(
            self.root,
            text=f"Add Habits",
            font=("Arial", 20, "bold"),
            background="white",
            width=55,
            height=2,
        )
        self.label.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

        self.btn_return = tk.Button(
            self.root, text="⏎", width=5, command=self.return_to_profile_page
        )
        self.btn_return.place(x=600, y=350)

        self.habit_entry = tk.Entry(self.root, width=50)
        self.habit_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.habit_type = tk.StringVar()
        self.habit_type.set("wanted")
        wanted_checkbox = tk.Radiobutton(
            self.root,
            text="Wanted Habit",
            variable=self.habit_type,
            value="wanted",
        )
        wanted_checkbox.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

        unwanted_checkbox = tk.Radiobutton(
            self.root,
            text="Unwanted Habit",
            variable=self.habit_type,
            value="unwanted",
        )
        unwanted_checkbox.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        self.timer_var = IntVar(value=0)
        timer_checkbox = tk.Checkbutton(
            self.root,
            text="Enable Timer",
            variable=self.timer_var,
            onvalue=1,
            offvalue=0,
            command=self.toggle_timer_entry,
        )
        timer_checkbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Set up time picker widgets, initially hidden
        self.time_picker_label = tk.Label(
            self.root,
            text="Select Time:",
            font=("Arial", 14),
            background="white",
        )
        self.time_picker_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.minute_var = tk.StringVar(value=0)
        self.second_var = tk.StringVar(value=0)

        self.minute_label = tk.Label(self.root, text="Minutes:")
        self.minute_spinner = tk.Spinbox(
            self.root, from_=0, to=59, textvariable=self.minute_var
        )
        self.second_label = tk.Label(self.root, text="Seconds:")
        self.second_spinner = tk.Spinbox(
            self.root, from_=0, to=59, textvariable=self.second_var
        )

        # Initially hide time picker widgets
        self.hide_time_picker()

        self.btn_add_habit = tk.Button(
            self.root, text="Add Habit", width=15, command=self.add_habit
        )
        self.btn_add_habit.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def toggle_timer_entry(self):
        if self.timer_var.get() == 1:
            self.show_time_picker()
        else:
            self.hide_time_picker()

    def show_time_picker(self):
        self.time_picker_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.minute_label.place(relx=0.4, rely=0.75, anchor=tk.CENTER)
        self.minute_spinner.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.second_label.place(relx=0.6, rely=0.75, anchor=tk.CENTER)
        self.second_spinner.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

    def hide_time_picker(self):
        self.time_picker_label.place_forget()
        self.minute_label.place_forget()
        self.minute_spinner.place_forget()
        self.second_label.place_forget()
        self.second_spinner.place_forget()

    def return_to_profile_page(self):
        self.destroy()
        self.profile_page.display_habits()

    def add_habit(self):
        habit_text = self.habit_entry.get()
        habit_type = self.habit_type.get()
        enable_timer = self.timer_var.get()
        timer_minutes = int(self.minute_var.get())
        timer_seconds = int(self.second_var.get())

        if habit_text and habit_type:
            self.habit_entry.delete(0, "end")

            habit_text_to_save = habit_text
            if habit_type == "unwanted":
                habit_text_to_save += " (Unwanted)"

            if enable_timer:
                if timer_minutes > 0 or timer_seconds > 0:
                    habit_text_to_save += f" (Timer: {timer_minutes} min {timer_seconds} sec)"
                else:
                    messagebox.showwarning("Warning", "Please enter a valid timer value.")
                    return

            self.profile_page.habits.append(habit_text_to_save)
            self.profile_page.save_habits()
            self.profile_page.display_habits()
            self.destroy()
        else:
            messagebox.showwarning("Warning", "Please enter a habit and select a type")

if __name__ == "__main__":
    root = tk.Tk()
    profile_selection = ProfileSelectionPage(root)
    root.mainloop()
