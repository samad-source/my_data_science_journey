import tkinter as tk
from tkinter import simpledialog, messagebox

# ATM DATA
balance = 1000
max_attempts = 4
attempt = 0

# CHECK BALANCE
def check_balance():
    global attempt

    # Check if transaction limit has been reached
    if attempt >= max_attempts:
        logout()
        return
    attempt += 1
    balance_label.config(
        text=f"Balance: ₦{balance:,}"
    )
    remaining = max_attempts - attempt
    if remaining == 0:
        messagebox.showinfo(
            "OMA Bank ATM",
            "You have used all 4 transactions."
        )
        logout()
    else:
        message_label.config(
            text=f"Balance checked. {remaining} transaction(s) remaining."
        )

# DEPOSIT
def deposit_money():
    global balance, attempt
    # Check transaction limit
    if attempt >= max_attempts:
        logout()
        return
    deposit = simpledialog.askinteger(
        "Deposit",
        "Enter your deposit amount:"
    )
    # User cancelled the input
    if deposit is None:
        return
    # Validate deposit
    if deposit <= 0:
        messagebox.showerror(
            "Invalid Deposit",
            "Deposit amount must be greater than zero."
        )
        return
    # Add money to balance
    balance += deposit
    attempt += 1
    balance_label.config(
        text=f"Balance: ₦{balance:,}"
    )
    remaining = max_attempts - attempt
    if remaining == 0:
        messagebox.showinfo(
            "Deposit Successful",
            f"₦{deposit:,} deposited successfully.\n\n"
            "You have used all 4 transactions."
        )
        logout()
    else:
        messagebox.showinfo(
            "Deposit Successful",
            f"₦{deposit:,} deposited successfully."
        )
        message_label.config(
            text=f"Deposit successful. {remaining} transaction(s) remaining."
        )

# WITHDRAW
def withdraw_money():
    global balance, attempt

    # Check transaction limit
    if attempt >= max_attempts:
        logout()
        return
    withdrawal = simpledialog.askinteger(
        "Withdrawal",
        "Enter your withdrawal amount:"
    )
    # User cancelled
    if withdrawal is None:
        return
    # Validate withdrawal amount
    if withdrawal <= 0:
        messagebox.showerror(
            "Invalid Withdrawal",
            "Withdrawal amount must be greater than zero."
        )
        return
    # Check balance
    if withdrawal > balance:
        messagebox.showerror(
            "Insufficient Balance",
            "Insufficient balance."
        )
        return
    # Subtract withdrawal from balance
    balance -= withdrawal
    attempt += 1
    balance_label.config(
        text=f"Balance: ₦{balance:,}"
    )
    remaining = max_attempts - attempt
    if remaining == 0:
        messagebox.showinfo(
            "Withdrawal Successful",
            f"₦{withdrawal:,} withdrawn successfully.\n\n"
            "You have used all 4 transactions."
        )
        logout()
    else:
        messagebox.showinfo(
            "Withdrawal Successful",
            f"₦{withdrawal:,} withdrawn successfully."
        )
        message_label.config(
            text=f"Withdrawal successful. {remaining} transaction(s) remaining."
        )

# LOGOUT
def logout():
    messagebox.showinfo(
        "OMA Bank ATM",
        "Thank you for using OMA Bank ATM."
    )
    window.destroy()

# MAIN WINDOW
window = tk.Tk()
window.title("OMA Bank ATM")
window.geometry("500x650")
window.resizable(True, True)

# TITLE
title_label = tk.Label(
    window,
    text="OMA BANK ATM",
    font=("Arial", 26, "bold")
)
title_label.pack(pady=30)

# WELCOME MESSAGE
welcome_label = tk.Label(
    window,
    text="Welcome to OMA Bank",
    font=("Arial", 16)
)
welcome_label.pack(pady=10)

# BALANCE DISPLAY
balance_label = tk.Label(
    window,
    text=f"Balance: ₦{balance:,}",
    font=("Arial", 22, "bold")
)
balance_label.pack(pady=20)

# MESSAGE
message_label = tk.Label(
    window,
    text="Please select an option",
    font=("Arial", 13)
)
message_label.pack(pady=10)

# CHECK BALANCE BUTTON
balance_button = tk.Button(
    window,
    text="CHECK BALANCE",
    width=20,
    height=2,
    font=("Arial", 12),
    command=check_balance
)
balance_button.pack(pady=10)

# DEPOSIT BUTTON
deposit_button = tk.Button(
    window,
    text="DEPOSIT",
    width=20,
    height=2,
    font=("Arial", 12),
    command=deposit_money
)
deposit_button.pack(pady=10)

# WITHDRAW BUTTON
withdraw_button = tk.Button(
    window,
    text="WITHDRAW",
    width=20,
    height=2,
    font=("Arial", 12),
    command=withdraw_money
)
withdraw_button.pack(pady=10)

# EXIT BUTTON
exit_button = tk.Button(
    window,
    text="EXIT",
    width=20,
    height=2,
    font=("Arial", 12),
    command=logout
)
exit_button.pack(pady=10)

# TRANSACTION COUNTER
attempt_label = tk.Label(
    window,
    text=f"Transactions allowed: {max_attempts}",
    font=("Arial", 11)
)
attempt_label.pack(pady=20)

# START APPLICATION
window.mainloop()