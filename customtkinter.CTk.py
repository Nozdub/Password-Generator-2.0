import customtkinter
import random

# sets color theme from json file in project folder.
customtkinter.set_default_color_theme("custom_theme.json")


# Allows usage of words stored in the txt file for the password creator.
file = open("words_alpha.txt", "r")
word_list = list(file.read().split("\n"))
wip_password = []


# CustomTkInter class.
# Could consider setting up text boxes and buttons in separate classes and then importing them.
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # setting up general size of window.
        self.geometry("720x300")
        self.title("Password Generator")
        self.minsize(300, 200)

        # create 3x3 grid system
        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure((0, 1), weight=2)

        # Initializing the customtkinter textbox.
        self.textbox_1 = customtkinter.CTkTextbox(master=self)
        self.textbox_1.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        # Initializing the customtkinter buttons.
        self.button = customtkinter.CTkButton(master=self, command=self.button_one_callback, text="Generate password")
        self.button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.button = customtkinter.CTkButton(master=self, command=self.button_event, text="Test password")
        self.button.grid(row=2, column=2, padx=10, pady=10, sticky="es")

    def button_one_callback(self):
        # Collects 4 random words from words list and appends to a list.
        for i in range(int(4)):
            part_one = random.choice(word_list)
            wip_password.append(part_one.capitalize())

        # Collects 4 random symbols from the symbols below and appends it to the list.
        for s in range(int(4)):
            symbols = ["@", "|", "#", "£", "$", "-", "_"]
            part_two = random.choice(symbols)
            wip_password.append(part_two)

        # Collects 4 random numbers from 0-9 and appends it to the list.
        for n in range(int(4)):
            numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            part_three = random.choice(numbers)
            wip_password.append(part_three)

        # Shuffles the password list.
        random.shuffle(wip_password)

        # Turns the password list into a string.
        completed_password = "".join(map(str, wip_password))

        # Prints password to textbox in GUI.
        self.textbox_1.insert("insert", completed_password + "\n")

        # Clears existing password for each click of the button.
        wip_password.clear()

    # WiP button, want to add check of password strength.
    def button_event(self):
        print("Hi. this functionality will be implemented later.")


# Initializes the GUI.
if __name__ == "__main__":
    app = App()
    app.mainloop()
