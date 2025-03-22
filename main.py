import tkinter as tk
from tkinter import messagebox
import random

# Function to roll the dice
def roll_dice():
    try:
        num_dice = int(num_dice_entry.get())
        dice_type = int(dice_type_var.get().lstrip('d'))
        
        if num_dice <= 0:
            raise ValueError("Can't roll no dice! Duh")
        
        if dice_type not in [4, 6, 8, 10, 12, 20]:
            raise ValueError("What do you think we are playing, Dungeon Crawl Classic")
        
        # Roll the dice
        rolls = [random.randint(1, dice_type) for _ in range(num_dice)]
        result_label.config(text=f"Results: {', '.join(map(str, rolls))}")
        total_label.config(text=f"Total: {sum(rolls)}")
    
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e.args[0]}")

# Function to clear the results
def clear_rolls():
    result_label.config(text="Results: ")
    total_label.config(text="Total: ")
    num_dice_entry.delete(0,tk.END)
    num_dice_entry.insert(0, "1")
    dice_type_var.set('d4')

# Set up the main window
root = tk.Tk()
root.title("Dice Roller")

# Label and Entry for number of dice
num_dice_label = tk.Label(root, text="Number of Dice:")
num_dice_label.grid(row=0, column=0, padx=10, pady=10)
num_dice_entry = tk.Entry(root)
num_dice_entry.insert(0, "1")
num_dice_entry.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for selecting dice type
dice_type_label = tk.Label(root, text="Dice Type:")
dice_type_label.grid(row=1, column=0, padx=10, pady=10)
dice_type_var = tk.StringVar(value='d4')
dice_type_menu = tk.OptionMenu(root, dice_type_var, 'd4', 'd6', 'd8', 'd10', 'd12', 'd20')
dice_type_menu.grid(row=1, column=1, padx=10, pady=10)

# Roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the results
result_label = tk.Label(root, text="Results: ")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display total
total_label = tk.Label(root, text="Total: ")
total_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_rolls)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()
