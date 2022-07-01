import tkinter as tk
from gui import login
from data import windows
import json

class App(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.gui_login = login.Login(self.root)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = App(root=root)
        app.mainloop()
    finally:
        windows.materials = 0
        windows.formulas = 0
        windows.inventory = 0
        windows.returns = 0
        windows.allocation = 0
        windows.manual_batch = 0
        windows.workoff = 0
        windows.work_orders = 0
        windows.recieving = 0
        windows.reports = 0
        windows.settings = 0
