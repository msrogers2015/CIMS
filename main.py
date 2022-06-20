import tkinter as tk
import scr.gui.login as glogin
import scr.gui.window as gwindow

class App(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.gui_login = glogin.Login(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root=root)
    app.mainloop()