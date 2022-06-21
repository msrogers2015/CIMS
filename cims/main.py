import tkinter as tk
import gui.login as glogin

class App(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.gui_login = glogin.Login(self.root,)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root=root)
    app.mainloop()