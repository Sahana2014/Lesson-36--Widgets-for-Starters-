#Here's the product
#Widgets for Starters!
#Write a Python program to create an application to take two numbers as input from the user and return the product using the Python Tkinter Library.
from tkinter import *

root = Tk()
root.title("Widgets for Starters!")
root.geometry("300x200")

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    label_result.config(text=f"Product: {product}")

label1 = Label(root, text="Enter first number:")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter second number:")
label2.pack()

entry2 = Entry(root)
entry2.pack()

button = Button(root, text="Calculate Product", command=calculate_product)
button.pack()

label_result = Label(root, text="Product: ")
label_result.pack()

root.mainloop()