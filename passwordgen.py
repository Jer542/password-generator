import tkinter as tk
import random
import string
import winsound

frequency = 750
duration = 1000

def generate_password(length, use_digits, use_special_chars):
    all_chars = string.ascii_letters
    if use_digits:
        all_chars += string.digits
    if use_special_chars:
        all_chars += string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def update_password():
    try:
        length = int(entry.get())
        if length < 10 or length > 64:
            password_label.config(text="Password length must be between 12 and 64.")
            return
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()
        password = generate_password(length, use_digits, use_special_chars)
        password_label.config(text=password)
        winsound.Beep(frequency, duration)
    except ValueError:
        password_label.config(text="Please enter a valid integer for length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    password_label.config(text="Password copied to clipboard!")
    root.bell()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PassGen")

    root.configure(bg='light grey')

    entry = tk.Entry(root)
    entry.pack(padx=20, pady=10)

    digits_var = tk.BooleanVar()
    digits_check = tk.Checkbutton(root, text="Include digits", variable=digits_var, bg='light grey')
    digits_check.pack(padx=20, pady=10)

    special_chars_var = tk.BooleanVar()
    special_chars_check = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var, bg='light grey')
    special_chars_check.pack(padx=20, pady=10)

    button = tk.Button(root, text="Generate Password", command=update_password, bg='light blue')
    button.pack(padx=20, pady=10)

    password_label = tk.Label(root, text="", bg='light grey')
    password_label.pack(padx=20, pady=10)

    copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='light blue')
    copy_button.pack(padx=20, pady=10)

    root.mainloop()