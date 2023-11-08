import tkinter as tk
import random

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create and place widgets
label = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
