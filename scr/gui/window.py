import tkinter as tk
import json

class Window(tk.Frame):
    def __init__(self, root=None):
        # Load json data
        data_json = open("scr/information/data.json")
        data = json.load(data_json)
        fonts = data["fonts"]
        data_json.close()
        super().__init__(root)
        self.root = root
        self.root.geometry("600x800")
        self.root.title("CIMS")
        # Creating widgets
        # Labels
        self.title = tk.Label(self.root, text=data["title"], font=tuple(fonts["title"]))
        self.version = tk.Label(self.root, text=data["version"], font=tuple(fonts["notes"]))
        # Buttons
        self.materials_btn = tk.Button(self.root, text="Materials", font=tuple(fonts["button"]))
        self.formulas_btn = tk.Button(self.root, text="Formulas", font=tuple(fonts["button"]))
        self.inventory_btn = tk.Button(self.root, text="Inventory", font=tuple(fonts["button"]))
        self.returns_btn = tk.Button(self.root, text="Returns", font=tuple(fonts["button"]))
        self.allocation_btn = tk.Button(self.root, text="Allocate", font=tuple(fonts["button"]))
        self.manual_batch_btn = tk.Button(self.root, text="Manual Allocation", font=tuple(fonts["button"]))
        self.workoff_btn = tk.Button(self.root, text="Workoff", font=tuple(fonts["button"]))
        self.work_orders_btn = tk.Button(self.root, text="Work Orders", font=tuple(fonts["button"]))
        self.recieving_btn = tk.Button(self.root, text="Recieving", font=tuple(fonts["button"]))
        self.reports_btn = tk.Button(self.root, text="Reports", font=tuple(fonts["button"]))
        self.settings_btn = tk.Button(self.root, text="Settings", font=tuple(fonts["button"]))
        self.support_btn = tk.Button(self.root, text="Support", font=tuple(fonts["button"]))
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
