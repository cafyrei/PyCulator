import customtkinter as ctk
from PIL import Image, ImageTk

# Centralized Window Pop
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    window.geometry(f"{width}x{height}+{x}+{y}")

# Program Functionality Methods
def clear_Button():
    screen.delete(0, ctk.END)

def press_Button(value):
    current = screen.get()
    screen.delete(0, ctk.END)
    screen.insert(0, current + value)

def calculate():
    try:
        expression = screen.get().replace('÷', '/').replace('×', '*')
        result = eval(expression)
        screen.delete(0, ctk.END)
        screen.insert(0, str(result))
    except Exception as e:
        screen.delete(0, ctk.END)
        screen.insert(0, "Syntax Error")

# Instance of a Window
window = ctk.CTk()

# Set appearance mode and theme
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

# Initialize the Calculator Screen
screen = ctk.CTkEntry(window, font=("Anonymous Pro", 25), justify="right")
screen.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5, padx=5)

# Buttons Initialization
buttons = [('C', 1, 0), ('()', 1, 1), ('%', 1, 2), ('÷', 1, 3),
           ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
           ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
           ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
           ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
        ]

# Button Screen Loading
for (label, row, col) in buttons:
    if label == 'C':
        button = ctk.CTkButton(window, text=label, font=("Anonymous Pro", 14), height=2, width=5, command=clear_Button)
    elif label == '=':
        button = ctk.CTkButton(window, text=label, font=("Anonymous Pro", 14), height=2, width=5, command=calculate)
    else:
        button = ctk.CTkButton(window, text=label, font=("Anonymous Pro", 14), height=2, width=5, command=lambda value=label: press_Button(value))
   
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Adjust the button size relative to the size of the window (Row)
for i in range(6):  # 6 rows
    window.grid_rowconfigure(i, weight=1)
    
# Adjust the button size relative to the size of the window (Column)
for j in range(4):  # 4 columns
    window.grid_columnconfigure(j, weight=1)

# Window Components Declaration     
window.title("PyCulator")
window.resizable(False, False)
center_window(window, 400, 500)
window.iconbitmap("assets\img\icon.ico")

window.mainloop()
