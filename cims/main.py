import tkinter as tk
from gui import login

class App(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.gui_login = login.Login(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root=root)
    app.mainloop()