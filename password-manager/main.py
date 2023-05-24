from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        finally:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Password saved successfully.")

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

#---------------------------- UI SETUP ------------------------------- #
BACKGROUND = "#C4DFAA"
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

#Website
website_label = Label(text="Website:", bg=BACKGROUND)
website_label.grid(column=0, row=1)

#website_entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

#email/username
username = Label(text="Email/Username:", bg=BACKGROUND)
username.grid(row=2, column=0)

#username entry
username_entry = Entry(width=21)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "mypass@me.com")

#password
password = Label(text="Password:", bg=BACKGROUND)
password.grid(column=0, row=3)

#password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

#Generate password
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3, sticky="EW")

#add button
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

#Search button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, columnspan=2, sticky="EW")



window.mainloop()