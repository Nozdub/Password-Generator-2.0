import tkinter

import customtkinter
import random

# sets color theme from json file in project folder.
customtkinter.set_default_color_theme("custom_theme.json")

# Allows usage of words stored in the txt file for the password creator.
file = open("words_alpha.txt", "r")
word_list = list(file.read().split("\n"))
wip_password = []
password_list = []


# CustomTkInter class.
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # setting up general size of window.
        self.geometry("720x300")
        self.title("Password Generator")
        self.minsize(300, 200)

        # setting alternate fonts
        self.my_font = customtkinter.CTkFont(family="Helvetica", weight="bold")

        # create 3x3 grid system
        self.grid_rowconfigure(0, weight=5)
        self.grid_columnconfigure(0, weight=5)

        # Initializing the customtkinter textbox.
        self.textbox_1 = customtkinter.CTkTextbox(master=self)
        self.textbox_1.grid(row=0, column=0, rowspan=1, columnspan=5, pady=(20, 0), sticky="nsew")

        # Initializing the customtkinter dropdown menus.

        self.combobox_1 = customtkinter.CTkOptionMenu(master=self, font=self.my_font, values=["1", "2", "3", "4", "5", "6", "7", "8", "9"])


        self.combobox_1.grid(row=2, column=1, padx=10, pady=10)
        self.label_one = customtkinter.CTkLabel(master=self, font=self.my_font, text="How many words would you like in your password?")
        self.label_one.grid(row=2, column=0)

        self.combobox_2 = customtkinter.CTkOptionMenu(master=self, font=self.my_font, values=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.combobox_2.grid(row=3, column=1, padx=10, pady=10, )
        self.label_two = customtkinter.CTkLabel(master=self, font=self.my_font, text="How many numbers would you like in your password?")
        self.label_two.grid(row=3, column=0)

        self.combobox_3 = customtkinter.CTkOptionMenu(master=self, font=self.my_font, values=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.combobox_3.grid(row=4, column=1, padx=10, pady=10, )
        self.label_three = customtkinter.CTkLabel(master=self, font=self.my_font, text="How many symbols would you like in your password?")
        self.label_three.grid(row=4, column=0)

        # Initializing the customtkinter buttons.
        self.button = customtkinter.CTkButton(master=self, font=self.my_font, command=self.button_one_callback, text="Generate password")
        self.button.grid(row=3, column=4, padx=10, pady=10)

        self.button = customtkinter.CTkButton(master=self, font=self.my_font, command=self.button_event, text="Save password")
        self.button.grid(row=4, column=4, padx=10, pady=10)

    def combobox_callback_one(self):
        return self.combobox_1.get()

    def combobox_callback_two(self):
        return self.combobox_2.get()

    def combobox_callback_three(self):
        return self.combobox_3.get()

    def button_one_callback(self):
        # Clears existing password for each click of the button.
        wip_password.clear()
        # Collects 4 random words from words list and appends to a list.
        for i in range(int(self.combobox_callback_one())):
            part_one = random.choice(word_list)
            wip_password.append(part_one.capitalize())

        # Collects 4 random symbols from the symbols below and appends it to the list.
        for s in range(int(self.combobox_callback_three())):
            symbols = ["@", "|", "#", "£", "$", "-", "_"]
            part_two = random.choice(symbols)
            wip_password.append(part_two)

        # Collects 4 random numbers from 0-9 and appends it to the list.
        for n in range(int(self.combobox_callback_two())):
            numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            part_three = random.choice(numbers)
            wip_password.append(part_three)

        # Shuffles the password list.
        random.shuffle(wip_password)

        # Turns the password list into a string.
        completed_password = "".join(map(str, wip_password))
        password_list.append("".join(map(str, wip_password)))

        # Prints password to textbox in GUI.
        self.textbox_1.insert("insert", completed_password + "\n")

    # Ads event to button click that stores the given passwords shown in textbox1 to a dictionary with user accounts as
    # keys.
    def button_event(self):
        stored_passwords = []
        for i in password_list:
            accounts = input("What account do you want the password stored to? ")
            password_dict = {f"{accounts}": f"{i}"}
            stored_passwords.append(password_dict)
        for u in stored_passwords:
            f = open("user_passwords.txt", "a")
            f.write(str(f"{u}\n"))
            f.close()

# Initializes the GUI.
if __name__ == "__main__":
    app = App()
    app.mainloop()
