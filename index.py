import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    label_result.config(text=f"Generated Password: {password}")

# GUI setup
root = tk.Tk()
root.title("Random Password Generator")

label_length = tk.Label(root, text="Password Length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack()

label_result = tk.Label(root, text="Generated Password: ")
label_result.pack()

root.mainloop()