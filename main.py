from tkinter import *
import calculator

# Constants
BUTTON_WIDTH = 8
BUTTON_HEIGHT = 2
FONT_TYPE = "Arial"
FONT_SIZE_LABEL = 20
FONT_SIZE_BUTTONS = 16
LABEL_FONT = (FONT_TYPE, FONT_SIZE_LABEL)
BUTTON_FONT = (FONT_TYPE, FONT_SIZE_BUTTONS)
CHARACTER_LIMIT = 27

# Creates a button with a given symbol set as its text and also the symbol it appends to the current expression
def create_button(symbol: str, column: int, row: int, columnspan: int = 1, rowspan: int = 1):
    button = Button(mainframe,
                     text=symbol,
                     height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=BUTTON_FONT,
                     command=lambda: calc.append_to(current_expr, symbol))
    button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
    return button

# Initialize the "model" class
calc = calculator.Calculator(CHARACTER_LIMIT)

# Initialize the main window
root = Tk()
root.title("Kalkulačka 3000")

# Initialize the canvas
mainframe = Frame(root, padx=12, pady=3)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Initialize the label serving as the the calculator's "main screen"
current_expr = StringVar()
current_expr_label = Label(mainframe,
                           textvariable=current_expr,
                           font=LABEL_FONT,
                           background=("#cccccc"),
                           pady=20, anchor="e",
                           borderwidth=2, relief="solid")
current_expr_label.grid(column=0, row=0, columnspan=4, sticky=(W, E))

# Initialize the calculator's buttons
create_button("(", 0, 1)
create_button(")", 1, 1)
ce_button = create_button("CE", 2, 1)
ce_button.config(command=lambda: calc.clear_expression(current_expr))
backspace_button = create_button("<X", 3, 1)
backspace_button.config(command=lambda: calc.remove_last_char(current_expr))
create_button("7", 0, 2)
create_button("8", 1, 2)
create_button("9", 2, 2)
create_button("+", 3, 2)
create_button("4", 0, 3)
create_button("5", 1, 3)
create_button("6", 2, 3)
create_button("-", 3, 3)
create_button("1", 0, 4)
create_button("2", 1, 4)
create_button("3", 2, 4)
create_button("×", 3, 4)
create_button("0", 0, 5)
create_button(",", 1, 5)
equals_button = create_button("=", 2, 5)
equals_button.config(command=lambda: calc.calculate(current_expr))
create_button(":", 3, 5)

# Create all keybinds to allow for keyboard control as well
root.bind("0", lambda x: calc.append_to(current_expr, "0"))
root.bind("1", lambda x: calc.append_to(current_expr, "1"))
root.bind("2", lambda x: calc.append_to(current_expr, "2"))
root.bind("3", lambda x: calc.append_to(current_expr, "3"))
root.bind("4", lambda x: calc.append_to(current_expr, "4"))
root.bind("5", lambda x: calc.append_to(current_expr, "5"))
root.bind("6", lambda x: calc.append_to(current_expr, "6"))
root.bind("7", lambda x: calc.append_to(current_expr, "7"))
root.bind("8", lambda x: calc.append_to(current_expr, "8"))
root.bind("9", lambda x: calc.append_to(current_expr, "9"))
root.bind("(", lambda x: calc.append_to(current_expr, "("))
root.bind(")", lambda x: calc.append_to(current_expr, ")"))
root.bind("+", lambda x: calc.append_to(current_expr, "+"))
root.bind("-", lambda x: calc.append_to(current_expr, "-"))
root.bind("*", lambda x: calc.append_to(current_expr, "×"))
root.bind("/", lambda x: calc.append_to(current_expr, ":"))
root.bind(",", lambda x: calc.append_to(current_expr, ","))
root.bind("<BackSpace>", lambda x: calc.remove_last_char(current_expr))
root.bind("<Delete>", lambda x: calc.clear_expression(current_expr))
root.bind("<Return>", lambda x: calc.calculate(current_expr))

root.mainloop()