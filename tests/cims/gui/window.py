import tkinter as tk
import json

class Window(tk.Frame):
    def __init__(self, root=None, login_frame=None):
        # Load json data
        data_json = open("cims/information/data.json")
        self.data = json.load(data_json)
        self.fonts = self.data["fonts"]
        data_json.close()
        super().__init__(root)
        self.login_frame = login_frame
        self.root = root
        
    def create_window(self):
        # Update window
        self.root.geometry("600x800")
        self.root.title("CIMS")
        # Clear frame
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        # Labels
        self.title = tk.Label(self.root, text=self.data["title"], font=tuple(self.fonts["title"]))
        self.version = tk.Label(self.root, text=self.data["version"], font=tuple(self.fonts["notes"]))
        # Buttons
        self.materials_btn = tk.Button(self.root, text="Materials", font=tuple(self.fonts["button"]))
        self.formulas_btn = tk.Button(self.root, text="Formulas", font=tuple(self.fonts["button"]))
        self.inventory_btn = tk.Button(self.root, text="Inventory", font=tuple(self.fonts["button"]))
        self.returns_btn = tk.Button(self.root, text="Returns", font=tuple(self.fonts["button"]))
        self.allocation_btn = tk.Button(self.root, text="Allocate", font=tuple(self.fonts["button"]))
        self.manual_batch_btn = tk.Button(self.root, text="Manual Allocation", font=tuple(self.fonts["button"]))
        self.workoff_btn = tk.Button(self.root, text="Workoff", font=tuple(self.fonts["button"]))
        self.work_orders_btn = tk.Button(self.root, text="Work Orders", font=tuple(self.fonts["button"]))
        self.recieving_btn = tk.Button(self.root, text="Recieving", font=tuple(self.fonts["button"]))
        self.reports_btn = tk.Button(self.root, text="Reports", font=tuple(self.fonts["button"]))
        self.settings_btn = tk.Button(self.root, text="Settings", font=tuple(self.fonts["button"]))
        self.support_btn = tk.Button(self.root, text="Support", font=tuple(self.fonts["button"]))
        # Placing Widgets
        # Labels
        self.title.place(x=25, y=25, width=550, height=50)
        self.version.place(x=10, y=765, width=100, height=25)
        # Buttons
        self.materials_btn.place(x=33, y=100, width=250, height=50)
        self.inventory_btn.place(x=33, y=210, width=250, height=50)
        self.allocation_btn.place(x=33, y=320, width=250, height=50)
        self.workoff_btn.place(x=33, y=430, width=250, height=50)
        self.reports_btn.place(x=33, y=540, width=250, height=50)
        self.settings_btn.place(x=33, y=650, width=250, height=50)
        self.formulas_btn.place(x=317, y=100, width=250, height=50)
        self.returns_btn.place(x=317, y=210, width=250, height=50)
        self.manual_batch_btn.place(x=317, y=320, width=250, height=50)
        self.work_orders_btn.place(x=317, y=430, width=250, height=50)
        self.recieving_btn.place(x=317, y=540, width=250, height=50)
        self.support_btn.place(x=317, y=650, width=250, height=50)
