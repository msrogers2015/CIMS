import sqlite3
import hashlib
from gui import menu, signup
import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root=None, login_window=None):
        # Database link
        self.db = None
        # Create app window reference
        self.root = root
        self.login_window = login_window
        self.select = '''SELECT * FROM employees WHERE employee_id = ?'''
        # Create connection to menu
        self.menu = menu.Menu(self.root, self.login_window)
    
    def hash_password(self, passwrd: str, e_id: str, salt: int):
        # Input your hashing code here
        pass

    def login(self, username, passwrd):
        try:
            # Variables
            passwrd = str(passwrd)
            e_id = str(username)
            # Connect to database
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            # Select record associated with the username
            cur.execute(self.select, (e_id,))
            user = cur.fetchone()
            # Extract salt from database
            salt = user[4]
            # Hash user input password
            hashed_password = self.hash_password(passwrd, e_id, salt)
            # Extract password from database
            db_password = user[3]
            if hashed_password == db_password:
                self.menu.create_window()
            else:
                messagebox.showerror('Bad Information', 'Incorrect password or username entered. Please try again')
        except TypeError:
            messagebox.showerror('No information','Please enter username and/or password')

