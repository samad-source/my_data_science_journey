import tkinter as tk
from tkinter import messagebox

max_attempts = 4
attempt = 0

current_number = ""
first_number = None
operator = None


def update_display(value: str) -> None:
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, value)
    display.config(state="readonly")


def add_number(number: str | int) -> None:
    global current_number
    current_number += str(number)
    update_display(current_number)


def add_decimal() -> None:
    global current_number

    if "." not in current_number:
        if current_number == "":
            current_number = "0"

        current_number += "."
        update_display(current_number)


def clear_display() -> None:
    global current_number, first_number, operator

    current_number = ""
    first_number = None
    operator = None
    update_display("")


def delete_number() -> None:
    global current_number

    current_number = current_number[:-1]
    update_display(current_number)


def choose_operator(selected_operator: str) -> None:
    global first_number, operator, current_number

    if current_number == "":
        return

    first_number = float(current_number)
    operator = selected_operator
    current_number = ""
    update_display("")


def calculate() -> None:
    global current_number, first_number, operator, attempt

    if first_number is None or operator is None or current_number == "":
        return

    second_number = float(current_number)

    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        if second_number == 0:
            messagebox.showerror(
                "Math Error",
                "You cannot divide by zero."
            )
            clear_display()
            return

        result = first_number / second_number

    else:
        return

    attempt += 1

    if result.is_integer():
        result = int(result)

    current_number = str(result)
    first_number = None
    operator = None

    update_display(current_number)

    remaining = max_attempts - attempt

    attempt_label.config(
        text=f"Calculations remaining: {remaining}"
    )

    if remaining == 0:
        messagebox.showinfo(
            "Casio Calculator",
            "You have used all 4 calculations."
        )
        window.destroy()


def coming_soon() -> None:
    pass


def exit_calculator() -> None:
    window.destroy()


window = tk.Tk()
window.title("Casio Calculator")
window.geometry("390x650")
window.resizable(False, False)
window.configure(bg="#0c0c0c")

bg_color = "#0c0c0c"
button_color = "#222222"
button_hover = "#3a3a3a"
text_color = "white"

button_style = {
    "font": ("Arial", 15, "bold"),
    "bg": button_color,
    "fg": text_color,
    "activebackground": button_hover,
    "activeforeground": text_color,
    "relief": "flat",
    "bd": 0
}

title_label = tk.Label(
    window,
    text="Casio Calculator",
    font=("Arial", 20, "bold"),
    bg=bg_color,
    fg=text_color
)
title_label.pack(pady=15)

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    width=15,
    state="readonly",
    bg="#111111",
    fg=text_color,
    readonlybackground="#111111",
    relief="flat",
    bd=0
)
display.pack(pady=10, ipady=12)

attempt_label = tk.Label(
    window,
    text="Calculations remaining: 4",
    font=("Arial", 11),
    bg=bg_color,
    fg=text_color
)
attempt_label.pack(pady=5)

keypad = tk.Frame(window, bg=bg_color)
keypad.pack(pady=15)

button_1 = tk.Button(
    keypad,
    text="1",
    width=6,
    height=2,
    command=lambda: add_number(1),
    **button_style
)
button_1.grid(row=3, column=0, padx=3, pady=3)

button_2 = tk.Button(
    keypad,
    text="2",
    width=6,
    height=2,
    command=lambda: add_number(2),
    **button_style
)
button_2.grid(row=3, column=1, padx=3, pady=3)

button_3 = tk.Button(
    keypad,
    text="3",
    width=6,
    height=2,
    command=lambda: add_number(3),
    **button_style
)
button_3.grid(row=3, column=2, padx=3, pady=3)

equals_button = tk.Button(
    keypad,
    text="=",
    width=6,
    height=2,
    command=calculate,
    **button_style
)
equals_button.grid(row=3, column=3, padx=3, pady=3)

button_4 = tk.Button(
    keypad,
    text="4",
    width=6,
    height=2,
    command=lambda: add_number(4),
    **button_style
)
button_4.grid(row=2, column=0, padx=3, pady=3)

button_5 = tk.Button(
    keypad,
    text="5",
    width=6,
    height=2,
    command=lambda: add_number(5),
    **button_style
)
button_5.grid(row=2, column=1, padx=3, pady=3)

button_6 = tk.Button(
    keypad,
    text="6",
    width=6,
    height=2,
    command=lambda: add_number(6),
    **button_style
)
button_6.grid(row=2, column=2, padx=3, pady=3)

add_button = tk.Button(
    keypad,
    text="+",
    width=6,
    height=2,
    command=lambda: choose_operator("+"),
    **button_style
)
add_button.grid(row=2, column=3, padx=3, pady=3)

button_7 = tk.Button(
    keypad,
    text="7",
    width=6,
    height=2,
    command=lambda: add_number(7),
    **button_style
)
button_7.grid(row=1, column=0, padx=3, pady=3)

button_8 = tk.Button(
    keypad,
    text="8",
    width=6,
    height=2,
    command=lambda: add_number(8),
    **button_style
)
button_8.grid(row=1, column=1, padx=3, pady=3)

button_9 = tk.Button(
    keypad,
    text="9",
    width=6,
    height=2,
    command=lambda: add_number(9),
    **button_style
)
button_9.grid(row=1, column=2, padx=3, pady=3)

subtract_button = tk.Button(
    keypad,
    text="−",
    width=6,
    height=2,
    command=lambda: choose_operator("-"),
    **button_style
)
subtract_button.grid(row=1, column=3, padx=3, pady=3)

button_0 = tk.Button(
    keypad,
    text="0",
    width=6,
    height=2,
    command=lambda: add_number(0),
    **button_style
)
button_0.grid(row=4, column=0, padx=3, pady=3)

decimal_button = tk.Button(
    keypad,
    text=".",
    width=6,
    height=2,
    command=add_decimal,
    **button_style
)
decimal_button.grid(row=4, column=1, padx=3, pady=3)

clear_button = tk.Button(
    keypad,
    text="C",
    width=6,
    height=2,
    command=clear_display,
    **button_style
)
clear_button.grid(row=0, column=0, padx=3, pady=3)

delete_button = tk.Button(
    keypad,
    text="DEL",
    width=6,
    height=2,
    command=delete_number,
    **button_style
)
delete_button.grid(row=0, column=1, padx=3, pady=3)

divide_button = tk.Button(
    keypad,
    text="÷",
    width=6,
    height=2,
    command=lambda: choose_operator("/"),
    **button_style
)
divide_button.grid(row=0, column=2, padx=3, pady=3)

multiply_button = tk.Button(
    keypad,
    text="×",
    width=6,
    height=2,
    command=lambda: choose_operator("*"),
    **button_style
)
multiply_button.grid(row=0, column=3, padx=3, pady=3)

coming_soon_button = tk.Button(
    keypad,
    text="PASS",
    width=6,
    height=2,
    command=coming_soon,
    **button_style
)
coming_soon_button.grid(row=4, column=2, padx=3, pady=3)

exit_button = tk.Button(
    keypad,
    text="EXIT",
    width=6,
    height=2,
    command=exit_calculator,
    **button_style
)
exit_button.grid(row=4, column=3, padx=3, pady=3)

window.mainloop()