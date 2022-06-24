import tkinter as tk
import json
from commands import signup

class Signup(tk.Frame):
    def __init__(self, root=None):
        # Load json file
        self.data = None
        self.fonts = None
        self.db = None
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.fonts = self.data['fonts']
            self.db = self.data['database']['location']
        super().__init__(root)
        self.root = root
        self.sc = signup.Signup()

    def create_window(self):
        self.signup_window = tk.Toplevel(self.root)
        self.signup_window.geometry('500x250')
        self.signup_window.title('Create an Account')
        # Labels
        self.fname = tk.Label(self.signup_window,
            text='First Name',
            anchor='w',
            font=tuple(self.fonts['label']))
        self.lname = tk.Label(self.signup_window,
            text='Last Name',
            anchor='w',
            font=tuple(self.fonts['label']))
        self.eid = tk.Label(self.signup_window,
            text='*Employee ID',
            anchor='w',
            font=tuple(self.fonts['label']))
        self.pwd = tk.Label(self.signup_window,
            text='*Password',
            anchor='w',
            font=tuple(self.fonts['label']))
        self.pwd_check = tk.Label(self.signup_window,
            text='*Re-enter Password',
            anchor='w',
            font=tuple(self.fonts['label']))
        # Buttons
        self.create = tk.Button(self.signup_window,
            text='Create Account',
            command = lambda: self.sc.add_user(
                pwd=self.pwd_entry.get(),
                pwd_check=self.pwd_check_entry.get(),
                fname=self.fname_entry.get(),
                lname=self.lname_entry.get(),
                eid=self.eid_entry.get()),
            font=tuple(self.fonts['button']))
        self.back = tk.Button(self.signup_window,
            text='Back',
            command= lambda: self.signup_window.destroy(),
            font=tuple(self.fonts['button']))
        # Entry boxes
        self.fname_entry = tk.Entry(self.signup_window)
        self.lname_entry = tk.Entry(self.signup_window)
        self.eid_entry = tk.Entry(self.signup_window)
        self.pwd_entry = tk.Entry(self.signup_window,show='*')
        self.pwd_check_entry = tk.Entry(self.signup_window,show='*')
        # Widget Placement
        # Label placement
        self.fname.place(x=10, y=20, height=25, width=200)
        self.lname.place(x=10, y=55, height=25, width=200)
        self.eid.place(x=10, y=90, height=25, width=200)
        self.pwd.place(x=10, y=125, height=25, width=200)
        self.pwd_check.place(x=10, y=160, height=25, width=200)
        # Entry placement
        self.fname_entry.place(x=210, y=20, height=30, width=275)
        self.lname_entry.place(x=210, y=55, height=30, width=275)
        self.eid_entry.place(x=210, y=90, height=30, width=275)
        self.pwd_entry.place(x=210, y=125, height=30, width=275)
        self.pwd_check_entry.place(x=210, y=160, height=30, width=275)
        # Place Buttons
        self.create.place(x=65, y=200, width=175, height=35)
        self.back.place(x=260, y=200, width=175, height=35)
            