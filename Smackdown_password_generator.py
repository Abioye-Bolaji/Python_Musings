import random
import string
import tkinter as tk
from tkinter import messagebox

def password_generator(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase # Setting the users initial characters to lowercase letters

# Condition statements for each parameter
# If the user selects uppercase letters, digits, or symbols, the characters are added to the list of characters
   
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error! You've not selected any characters for your password."

    password = "".join(random.choice(characters) for _ in range(length)) # Concatenates the users choice through list comprehension
    return password

def generate_password(): # Function to generate the password
# Try and except block to handle invalid inputs

    try:
        length = int(length_entry.get())
        use_upper = upper_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        password = password_generator(length, use_upper, use_digits, use_symbols)
        result_label.config(text=f'Your password is: {password}')
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for the password length.")

def run_cli(): # Function to run the command line interface
    print('Welcome to Smackdown Password Generator🔐!')

    try:
        length = int(input('Enter your desired password length: '))
        use_upper = input("Would you like uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = password_generator(length, use_upper, use_digits, use_symbols)
        print(f'Your password is: {password}')
    except ValueError:
        print('Invalid input! Please enter a number for the password length.')

def run_gui(): # Function to run the graphical user interface
    root = tk.Tk()
    root.title("Smackdown Password Generator")

    tk.Label(root, text="Enter your desired password length:").pack()
    global length_entry
    length_entry = tk.Entry(root)
    length_entry.pack()

    global upper_var
    upper_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Include uppercase letters", variable=upper_var).pack()

    global digits_var
    digits_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Include digits", variable=digits_var).pack()

    global symbols_var
    symbols_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Include symbols", variable=symbols_var).pack()

    tk.Button(root, text="Generate Password", command=generate_password).pack()

    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__": #Condition where user selects the mode of the application
    mode = input("Enter 'cli' to run the command-line interface or 'gui' to run the graphical user interface: ").strip().lower()
    if mode == 'cli':
        run_cli()
    elif mode == 'gui':
        run_gui()
    else:
        print("Invalid mode selected. Please enter 'cli' or 'gui'.")