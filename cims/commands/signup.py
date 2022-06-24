import random
import json
import sqlite3
from . import login
from tkinter import messagebox

class Signup:
    def __init__(self, root=None):
        self.db = None
        self.login = login.Login()
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.fonts = self.data['fonts']
            self.db = self.data['database']['location']
        self.select = '''SELECT * FROM employees WHERE eid = ?;'''
        self.insert = '''INSERT INTO employees 
            (eid, fname, lname, pwd, salt)
            VALUES(?, ?, ?, ?, ?);'''

    def make_salt(self):
        key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-="
        salt = ''
        for x in range(16):
            salt += key[random.randint(0, 76)]
        return salt

    def add_user(self, pwd, pwd_check, fname, lname, eid):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        if pwd == pwd_check:
            cur.execute(self.select, (eid,))
            record = cur.fetchone()
            if record == None:
                salt = self.make_salt()
                pwd = self.login.hash_password(pwd, eid, salt)
                if eid != '' and pwd != '':
                    cur.execute(self.insert, (eid, fname, lname, pwd, salt)) 
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('User Added','New user has been added'\
                        ' to the database.')         
            else:
                messagebox.showwarning('User Exist','A user with this employee id '\
                'already exists.')
        else:
            messagebox.showerror('Wrong Passowrd','Passwords do not match.')