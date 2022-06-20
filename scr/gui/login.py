import tkinter as tk
import json


class Login(tk.Frame):
    def __init__(self, root=None):
        # Load json data
        data_json = open("scr/information/data.json")
        data = json.load(data_json)
        fonts = data["fonts"]
        data_json.close()
        super().__init__(root)
        # Creating root association
        self.root = root
        # Updating window information
        self.root.geometry("600x300")
        self.root.title("CIMS Login")
        # Creating all widgets for screen
        # Labels
        self.title = tk.Label(self.root, text=data["title"], font=tuple(fonts["title"]))
        self.username = tk.Label(self.root, text="Username", font=tuple(fonts["label"]))
        self.pssword = tk.Label(self.root, text="Password", font=tuple(fonts["label"]))
        self.version = tk.Label(self.root, text=data["version"], font=tuple(fonts["notes"]))
        # Entry boxes
        self.user_entry = tk.Entry(self.root)
        self.pw_entry = tk.Entry(self.root)
        # Buttons
        self.login_btn = tk.Button(self.root, text="Login", font=tuple(fonts["button"]))
        self.sign_btn = tk.Button(self.root, text="Sign Up", font=tuple(fonts["button"]))
        self.forgot_btn = tk.Button(self.root, text="Forgot Password", font=tuple(fonts["button"]))
        # Placing Widgets
        # Labels
        self.title.place(x=25, y=25, width=550, height=50)
        self.username.place(x=75, y=100, width=150, height=30)
        self.pssword.place(x=75, y=130, width=150, height=30)
        self.version.place(x=10, y=270, width=100, height=25)
        # Entry boxes
        self.user_entry.place(x=225, y=100, width=300, height=30)
        self.pw_entry.place(x=225, y=130, width=300, height=30)
        # Buttons
        self.login_btn.place(x=75, y=190, width=85, height=30)
        self.sign_btn.place(x=205, y=190, width=90, height=30)
        self.forgot_btn.place(x=345, y=190, width=175, height=30)
        