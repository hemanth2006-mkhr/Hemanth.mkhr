from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# Import tkinter module for GUI
import tkinter as tk

# Create a window object
window = tk.Tk()
window.title("Calculator App")

# Create a global variable to store the expression
expression = ""

# Define a function to update the expression
def update_expression(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Define a function to evaluate the expression
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Define a function to clear the expression
def clear_expression():
    global expression
    expression = ""
    equation.set("")

# Create a string variable to display the equation
equation = tk.StringVar()
equation.set("")

# Create a label to show the equation
equation_label = tk.Label(window, textvariable=equation)
equation_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits and operators
button_1 = tk.Button(window, text="1", command=lambda: update_expression(1))
button_2 = tk.Button(window, text="2", command=lambda: update_expression(2))
button_3 = tk.Button(window, text="3", command=lambda: update_expression(3))
button_4 = tk.Button(window, text="4", command=lambda: update_expression(4))
button_5 = tk.Button(window, text="5", command=lambda: update_expression(5))
button_6 = tk.Button(window, text="6", command=lambda: update_expression(6))
button_7 = tk.Button(window, text="7", command=lambda: update_expression(7))
button_8 = tk.Button(window, text="8", command=lambda: update_expression(8))
button_9 = tk.Button(window, text="9", command=lambda: update_expression(9))
button_0 = tk.Button(window, text="0", command=lambda: update_expression(0))
button_plus = tk.Button(window, text="+", command=lambda: update_expression("+"))
button_minus = tk.Button(window, text="-", command=lambda: update_expression("-"))
button_multiply = tk.Button(window, text="*", command=lambda: update_expression("*"))
button_divide = tk.Button(window, text="/", command=lambda: update_expression("/"))
button_equal = tk.Button(window, text="=", command=evaluate_expression)
button_clear = tk.Button(window, text="C", command=clear_expression)

# Arrange the buttons in a grid layout
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Run the main loop of the window
window.mainloop()
