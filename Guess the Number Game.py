import random
import tkinter as tk
from tkinter import messagebox

def guess_the_number():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    result_label.config(text="I have selected a number between 1 and 100. Take a guess!")

def check_guess():
    global attempts
    guess = int(entry.get())
    attempts += 1
    if guess < number_to_guess:
        result_label.config(text="Too low! Try again.")
    elif guess > number_to_guess:
        result_label.config(text="Too high! Try again.")
    else:
        messagebox.showinfo("Congratulations!", f"You've guessed the number in {attempts} attempts.")
        guess_the_number()

root = tk.Tk()
root.title("Guess the Number Game")

entry = tk.Entry(root)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

guess_the_number_button = tk.Button(root, text="Start New Game", command=guess_the_number)
guess_the_number_button.pack(pady=10)

guess_the_number()

root.mainloop()