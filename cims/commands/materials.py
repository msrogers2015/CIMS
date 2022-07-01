from cgitb import enable
import sqlite3
import json
from tkinter import messagebox
from data import windows

class Materials:
    def __init__(self):
        self.db = None
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.db = self.data['database']['location']
        self.add_SQL = '''INSERT INTO materials (
                    mid, name, health, flammibility, reactivity, ppe,
                    description, comment, vender, system, weight, cost,
                    reorder, low_stock, lvalue, avalue, bvalue)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    
    def add(self, material_information: list):
        pass


    def update(self, *args):
        pass

    def delete(self, material):
        pass

    def exit(self, window):
        windows.materials = 0
        window.destroy()

    def update_color(self, l, a, b):
        pass
