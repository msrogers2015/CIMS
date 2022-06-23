import sqlite3
import hashlib
from gui import window 

class Login:
    def __init__(self, root=None, login_window=None, database=None):
        # Create main menu window
        self.root = root
        self.login_window = login_window
        self.menu = window.Window(self.root, self.login_window)
        # Create database connection
        self.con = sqlite3.connect('cims/database/cims.db')
        # Preformatted SQL snippets
        self.insert_sql = '''INSERT INTO employees 
            (employee_id, first_name, last_name, password, salt)
            VALUES(?, ?, ?, ?, ?);'''
        self.select_sql = '''SELECT * FROM employees WHERE employee_id = ?;'''

    def hash_password(self, passwrd: str, id: int, salt: str):
        string_to_hash = str(id) + passwrd + salt
        hash_byte = bytes(string_to_hash, 'utf-8')
        m = hashlib.sha256()
        m.update(hash_byte)
        m.digest()
        return str(m.hexdigest())
    
    def login(self, username, passwrd):
        # Create database cursor
        self.cur = self.con.cursor()
        # Run SQL command
        self.cur.execute(self.select_sql,(username, ))
        # Retrieve a single record
        db_entry = self.cur.fetchone()
        # Create variables
        hashed_database = db_entry[3]
        hashed_password = self.hash_password(passwrd, db_entry[0], db_entry[4])
        if hashed_database == hashed_password:
            # add code to open main menu
            self.menu.create_window()
        else:
            # add code to alert wrong password
            print('False')