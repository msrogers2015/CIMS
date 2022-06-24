import tkinter as tk
import json
from commands import login as cl
from gui import signup
from tkinter import messagebox

class Login(tk.Frame):
    def __init__(self, root=None):
        # Load json file
        self.data = None
        self.fonts = None
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.fonts = self.data['fonts']
        # Load app window
        super().__init__(root)
        self.root = root
        # Update window name and size
        self.root.geometry('600x300')
        self.root.title('CIMS Login')
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(expand=True, fill='both')
        # Import commands
        self.cl = cl.Login(self.root, self.login_frame)
        self.signup = signup.Signup(self.root)
        self.create_window()

    def create_window(self):
        '''Creation and placement of all tkinter widgets for login screen.'''
        # Labels
        self.title = tk.Label(
            self.login_frame,
            text=self.data["title"],
            font=tuple(self.fonts["title"])
        )
        self.username = tk.Label(
            self.login_frame,
            text="Username",
            font=tuple(self.fonts["label"])
        )
        self.pssword = tk.Label(
            self.login_frame,
            text="Password",
            font=tuple(self.fonts["label"])
        )
        self.version = tk.Label(
            self.login_frame,
            text=self.data["version"],
            font=tuple(self.fonts["notes"])
        )
        # Entry boxes
        self.user_entry = tk.Entry(self.login_frame)
        self.pw_entry = tk.Entry(self.login_frame, show="*")
        # Buttons
        self.login_btn = tk.Button(
            self.login_frame,
            text="Login",
            font=tuple(self.fonts["button"]),
            command=lambda: self.cl.login(
                username=self.user_entry.get(), 
                passwrd=self.pw_entry.get()
            )
        )
        self.sign_btn = tk.Button(
            self.login_frame,
            text="Sign Up",
            font=tuple(self.fonts["button"]),
            command =lambda: self.signup.create_window())
        self.forgot_btn = tk.Button(
            self.login_frame,
            text="Forgot Password",
            font=tuple(self.fonts["button"]),
            command= lambda: self.forgot_password()
        )
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

    def forgot_password(self):
        messagebox.showinfo('Forgot Password',
            'Contact your employer for a password reset')