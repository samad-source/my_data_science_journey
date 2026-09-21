import tkinter as tk
from tkinter import messagebox
import random

secret_number = random.randint(1, 101)
guess = None


def check_guess():
    global guess

    try:
        guess = int(guess_entry.get())
    except ValueError:
        message_label.config(text="Please enter a number from 1 to 100.")
        return

    if guess < 1 or guess > 100:
        message_label.config(text="Please enter a number from 1 to 100.")
        return

    if guess < secret_number:
        message_label.config(text="Number too Low !!!")

    elif guess > secret_number:
        message_label.config(text="Number too High !!!")

    else:
        message_label.config(text="Correct Guess!!!")
        messagebox.showinfo(
            "Congratulations",
            f"Correct! The number was {secret_number}."
        )


def new_game():
    global secret_number, guess

    secret_number = random.randint(1, 101)
    guess = None

    guess_entry.delete(0, tk.END)
    message_label.config(text="Guess a number from 1 to 100.")


window = tk.Tk()
window.title("Guessing Game")
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg="#0c0c0c")


title_label = tk.Label(
    window,
    text="GUESSING GAME",
    font=("Arial", 24, "bold"),
    bg="#0c0c0c",
    fg="white"
)
title_label.pack(pady=30)


instruction_label = tk.Label(
    window,
    text="Guess a number between 1 and 100",
    font=("Arial", 14),
    bg="#0c0c0c",
    fg="white"
)
instruction_label.pack(pady=10)


guess_entry = tk.Entry(
    window,
    font=("Arial", 22),
    justify="center",
    width=10,
    bg="#1c1c1c",
    fg="white",
    insertbackground="white",
    relief="flat"
)
guess_entry.pack(pady=15)


guess_button = tk.Button(
    window,
    text="GUESS",
    font=("Arial", 14, "bold"),
    width=15,
    height=2,
    bg="#222222",
    fg="white",
    activebackground="#3a3a3a",
    activeforeground="white",
    relief="flat",
    command=check_guess
)
guess_button.pack(pady=10)


message_label = tk.Label(
    window,
    text="Guess a number from 1 to 100.",
    font=("Arial", 14, "bold"),
    bg="#0c0c0c",
    fg="white"
)
message_label.pack(pady=20)


new_game_button = tk.Button(
    window,
    text="NEW GAME",
    font=("Arial", 12, "bold"),
    width=15,
    height=2,
    bg="#222222",
    fg="white",
    activebackground="#3a3a3a",
    activeforeground="white",
    relief="flat",
    command=new_game
)
new_game_button.pack(pady=10)


window.mainloop()