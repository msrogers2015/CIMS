import sqlite3
import json
from gui import materials
from tkinter import messagebox

class Materials:
    def __init__(self, window=None):
        self.db = None
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.db = self.data['database']['location']
        self.menu = window
    
    def add(self, *args):
        pass

    def update(self, *args):
        pass

    def delete(self, material):
        pass

    def exit(self):
        pass

    def update_color(self, l, a, b):
        pass