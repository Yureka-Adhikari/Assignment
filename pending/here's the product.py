import tkinter as tk

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Multiplication App")
root.geometry("300x200")
root.configure(bg="lavender")

tk.Label(root, text="Enter first number:", fg="indigo", bg="lavender").pack()
entry1 = tk.Entry(root, fg="indigo", bg="lavender")
entry1.pack()

tk.Label(root, text="Enter second number:", fg="indigo", bg="lavender").pack()
entry2 = tk.Entry(root, fg="indigo", bg="lavender")
entry2.pack()

tk.Button(root, text="Multiply", command=multiply, fg="indigo", bg="lavender").pack()

result = tk.StringVar()
tk.Label(root, text="Result:", fg="indigo", bg="lavender").pack()
tk.Label(root, textvariable=result, fg="indigo", bg="lavender").pack()

root.mainloop()