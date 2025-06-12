from tkinter import *
import datetime

def calculate_age():
    try:
        birth_date = datetime.datetime.strptime(entry.get(), "%Y-%m-%d")
        today = datetime.datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid date format. Use YYYY-MM-DD.")

root = Tk()
root.title("Age Calculator")
root.geometry("300x200")
root.configure(bg="lavender")

label = Label(root, text="Enter your birth date (YYYY-MM-DD):", fg="blue", bg="lavender")
label.pack(pady=10)
entry = Entry(root, width=20, fg="blue", bg="lavender")
entry.pack(pady=5)
calculate_button = Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)
result_label = Label(root, text="",  fg="blue", bg="lavender")
result_label.pack(pady=10)

root.mainloop()