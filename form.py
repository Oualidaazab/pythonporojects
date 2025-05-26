import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if name and email and age:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nAge: {age}")
        print(f"Name: {name}, Email: {email}, Age: {age}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create the main window
window = tk.Tk()
window.title("Simple Form")
window.geometry("300x250")

# Create form labels and entries
tk.Label(window, text="Name").pack(pady=5)
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

tk.Label(window, text="Email").pack(pady=5)
email_entry = tk.Entry(window)
email_entry.pack(pady=5)

tk.Label(window, text="Age").pack(pady=5)
age_entry = tk.Entry(window)
age_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the GUI event loop
window.mainloop()
