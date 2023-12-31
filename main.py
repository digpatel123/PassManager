from tkinter import *
import random
import string
import json
from tkinter import messagebox


def save_data(website, email, password):
    data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as file:
            # Reading the data
            read_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        read_data = {}

    # Updating the data
    read_data.update(data)

    with open("data.json", "w") as file:
        # Writing the data
        json.dump(read_data, file, indent=4)


def search_data(website):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data was found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Search Result", f"No password for {website} was found.")


def generate_password():
    password_length = 8
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    return password


def create_form():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    canvas = Canvas(window, height=200, width=200)
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
    canvas.grid(row=0, column=0, columnspan=4)

    def add_data():
        website = website_entry.get()
        email = email_entry.get()
        password = pass_entry.get()

        if website == "" or email == "" or password == "":
            messagebox.showerror("Error", "Please enter all the details to add to your data file.")
        else:
            confirmation_message = f"Website: {website}\nEmail/Username: {email}\nPassword: {password}"
            response = messagebox.askquestion("Confirmation", confirmation_message)
            if response == "yes":
                save_data(website, email, password)
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

    def generate_and_insert_password():
        password = generate_password()
        pass_entry.delete(0, END)
        pass_entry.insert(0, password)

        # Finding the password using website entry
    def search_website():
        website = website_entry.get()
        if website == "":
            messagebox.showerror("Error", "Please enter a website name to search.")
        else:
            search_data(website)

    # Creating labels
    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0, sticky="e")
    email_label = Label(text="Email/Username:")
    email_label.grid(row=2, column=0, sticky="e")
    pass_label = Label(text="Password")
    pass_label.grid(row=3, column=0, sticky="e")

    # Creating Textboxes
    website_entry = Entry(width=35)
    website_entry.grid(row=1, column=1, sticky="e")
    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2, sticky="we")
    email_entry.insert(0, "dj@dj.com")
    pass_entry = Entry(width=21)
    pass_entry.grid(row=3, column=1, sticky="w")

    # Creating buttons
    gen_pass_button = Button(text="Generate password", command=generate_and_insert_password)
    gen_pass_button.grid(row=3, column=2, sticky="e")
    add_button = Button(text="Add", width=10, command=add_data)
    add_button.grid(row=4, column=1, sticky="we")

    search_button = Button(text="Search", width=10, command=search_website)
    search_button.grid(row=1, column=2, sticky="e")

    window.mainloop()


# Call the function you want to execute
create_form()
