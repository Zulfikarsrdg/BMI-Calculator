from tkinter import *
from tkinter.ttk import Style, Entry, Label

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=200)

my_label = Label(text="Enter Your Weight (kg)")
my_label.pack()

entry = Entry(width=20)
entry.pack()

my_label2 = Label(text="Enter Your Height (cm)")
my_label2.pack()

entry2 = Entry(width=20)
entry2.pack()

def button_clicked():
    weight = entry.get()
    height = entry2.get()

    if not weight.isdigit():
        result_label.config(text="Please enter a valid weight.", foreground="red")
        return

    if not height.isdigit():
        result_label.config(text="Please enter a valid height.", foreground="red")
        return

    weight = float(weight)
    height = float(height) / 100
    result = weight / (height * height)

    if result < 18.5:
        result_label.config(text="Underweight", foreground="yellow")
    elif 18.5 <= result < 24.9:
        result_label.config(text="Normal", foreground="green")
    elif 25 <= result < 29.9:
        result_label.config(text="Overweight", foreground="orange")
    elif 30 <= result < 34.9:
        result_label.config(text="Obese (Type 1)", foreground="lightcoral")
    elif 35 <= result < 39.9:
        result_label.config(text="Obese (Type 2)", foreground="red")
    elif result >= 40.0:
        result_label.config(text="Severely Obese (Type 3)", foreground="darkred")


my_button = Button(text="Calculate", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

result_label = Label(text="")
result_label.pack()

window.mainloop()
