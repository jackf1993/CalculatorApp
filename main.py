# Author: Jack Farah
# Title: Calculator
# Description: A fully functional calculator with a few operators including
#              ['+', "-", ' *', '/', '*3.14', "%", "(", ")", "**", "**2"]
#               using the tkinter library for GUI and ast for string comprehension

# Import necessary libraries
from tkinter import *
import ast

# tkinter object
root = Tk()

# global counter for display index
i = 0


# function to insert what is currently in display.
# this will be used to display integers on calculator
def get_num(num):
    global i
    display.insert(i, num)
    i += 1


# function to insert the operator into display
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# function to clear the display aka AC button
def clear_all():
    display.delete(0, END)


# function to convert the display as a string to a literal equation using asl library
def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# function to remove the most resent input on display
def back():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")


# creating a display object
display = Entry(root)
# Determining the location of the display
display.grid(row=1, columnspan=6)

# variable names numbers to determine the approved integers for the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# counter variable to help the function assign the necessary number per button
counter = 0
# nested for loop to automate the numbers 1-9
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=3, height=2, command=lambda text=button_text: get_num(text))
        button.grid(row=x + 2, column=y)
        counter += 1

# creating the 0 individually to set its location under the 8
button = Button(root, text='0', width=2, height=2, command=lambda: get_num(0))
button.grid(row=5, column=1)

count = 0
operations = ['+', "-", ' *', '/', '*3.14', "%", "(", ")", "**", "**2"]

# same process as setting the numbers, but now we are setting the operators
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=3, height=2,
                            command=lambda text=operations[count]: get_operation(text))
            count += 1
            button.grid(row=x + 2, column=y + 3)

# individually creating the AC, =, and <- (back) buttons to their specified locations
Button(root, text='AC', width=3, height=2, command=clear_all).grid(row=5, column=0)
Button(root, text='=', width=3, height=2, command=calculate).grid(row=5, column=2)
Button(root, text='<-', width=3, height=2, command=lambda: back()).grid(row=5, column=4)

root.mainloop()
