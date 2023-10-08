import customtkinter as tk
import customtkinter
import string
import random
import pyperclip

def generate_password():

    password_length = int(length_entry.get())



    password_chars = string.ascii_letters
    if include_numbers.get():
        password_chars += string.digits
    if include_special_chars.get():
        password_chars += string.punctuation
    


    password = ''.join(random.choice(password_chars) for i in range(password_length))


    password_label.configure(text = password)



root = tk.CTk()
root.title("Password Generator")
root.geometry("320x200")

customtkinter.set_default_color_theme("green")

include_numbers =  tk.BooleanVar()
include_special_chars = tk.BooleanVar()


length_entry = tk.CTkEntry(root, font=("Arial", 14))
length_entry.pack(pady = 10)


lenght_label = tk.CTkLabel(root, text="Password Length:", font=("Arial", 14))
lenght_label.pack(pady = 5)


generate_button = tk.CTkButton(root, text="Generate", font= ("Arial", 14), command=generate_password)
generate_button.pack(pady=10)


password_label = tk.CTkLabel(root, text="", font=("Arial", 14))
password_label.pack(pady=10)



root.mainloop()