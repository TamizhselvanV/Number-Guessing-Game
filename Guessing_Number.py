import tkinter as tk
import random

# Generate the secret number
secret_number = random.randint(1, 100)
attempts = 0

# Check guess function
def check_guess():
    global attempts
    guess = entry.get()
    if not guess.isdigit():
        result_label.config(text="❌ Enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        result_label.config(text="🔼 Too low! Try again.")
    elif guess > secret_number:
        result_label.config(text="🔽 Too high! Try again.")
    else:
        result_label.config(
            text=f"🎉 Correct! You guessed it in {attempts} attempts.")

# Restart the game
def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Guess a number between 1 and 100")

# Set up the GUI
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#f5f5f5")

title = tk.Label(root, text="🎯 Number Guessing Game", font=("Arial", 18, "bold"), bg="#f5f5f5")
title.pack(pady=10)

instruction = tk.Label(root, text="Enter a number between 1 and 100:", font=("Arial", 12), bg="#f5f5f5")
instruction.pack()

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("Arial", 12), bg="#4CAF50", fg="white", command=check_guess)
check_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart", font=("Arial", 12), bg="#f44336", fg="white", command=restart_game)
restart_button.pack(pady=5)

result_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14), bg="#f5f5f5", fg="#333")
result_label.pack(pady=20)

root.mainloop()
