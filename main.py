from time import strftime
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project from Day 5 refactored
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password = []

    [password.append(choice(LETTERS)) for _ in range(0, randint(8, 10))]
    [password.append(choice(SYMBOLS)) for _ in range(0, randint(2, 6))]
    [password.append(choice(NUMBERS)) for _ in range(0, randint(2, 6))]

    shuffle(password)
    password = "".join(password)
    pwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    global website_entry, user_entry, pwd_entry
    website = website_entry.get()
    user = user_entry.get()
    pwd = pwd_entry.get()

    if len(website) == 0 or len(user) == 0 or len(pwd) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {user}\n"
                                                              f"Password: {pwd}"
                                                              f" \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{strftime('%a %d %b %Y, %I:%M%p')} | {website} | {user} | {pwd}\n")
            reset_ui()


def reset_ui():
    global website_entry, user_entry, pwd_entry
    website_entry.delete(0, END)
    pwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas Docs: https://tkdocs.com/tutorial/canvas.html
canvas = Canvas(height=200, width=200)
pwd_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pwd_img)
canvas.grid(column=1, row=0)
# columnspan = how many cols do you want the item to span over

# Labels on left side
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pwd_label = Label(text="Password:")
pwd_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=42)
user_entry.insert(0, "katrinaemily.best@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2)

pwd_entry = Entry(width=30)
pwd_entry.grid(column=1, row=3)

# Buttons
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
