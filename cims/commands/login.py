import sqlite3
import json
import hashlib
from gui import menu, signup
import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, root=None, login_window=None):
        # Get database information from json file
        self.db = ''
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.db = self.data['database']['location']
        # Create app window reference
        self.root = root
        self.login_window = login_window
        self.select = '''SELECT * FROM employees WHERE eid = ?'''
        # Create connection to menu
        self.menu = menu.Menu(self.root, self.login_window)
    
    def hash_password(self, passwrd: str, e_id: str, salt: str):
        password_to_hash = e_id + passwrd + salt
        password_byte = bytes(password_to_hash, 'utf-8')
        hash = hashlib.sha256()
        hash.update(password_byte)
        hash.digest()
        return hash.hexdigest()


    def login(self, username, passwrd):
        try:
            # Variables
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
            conn.close()
            if hashed_password == db_password:
                self.menu.create_window()
            else:
                messagebox.showerror('Bad Information', 'Incorrect password or username entered. Please try again')
        except TypeError as e:
            messagebox.showerror('Bad Information','Please check username and or password.')

