import tkinter as tk
import json
from turtle import right

class Materials(tk.Frame):
    def __init__(self, root=None, menu=None):
        self.data = None
        self.fonts = None
        self.db = None
        with open('cims/data/data.json') as f:
            self.data = json.load(f)
            self.fonts = self.data['fonts']
            self.db = self.data['database']['location']
        super().__init__(root)
        self.root = root
        self.menu = menu
        self.create_window()

    def create_window(self):
        # Create Window
        self.window = tk.Toplevel(self.root)
        self.window.geometry('800x650')
        self.window.title('CIMS - Materials')
        # Create Widgets
        # Labels
        self.material_id = tk.Label(self.window,
            text='Material ID',
           font=tuple(self.fonts["label"]),
           anchor="w"
        )
        self.name = tk.Label(self.window,
            text='Name',
           font=tuple(self.fonts["label"]),
           anchor="w"
        )
        self.health = tk.Label(self.window,
            text='Health', justify='left',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.flammability = tk.Label(self.window,
            text='Flammability', justify='left',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.reactivity = tk.Label(self.window,
            text='Reactivity', justify='left',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.ppe = tk.Label(self.window,
            text='PPE', justify='left',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.description = tk.Label(self.window,
            text='Description',
           font=tuple(self.fonts["notes"]),
           anchor='w'
        )
        self.comments = tk.Label(self.window,
            text='Comments',
           font=tuple(self.fonts["notes"]),
           anchor='w'
        )
        self.vendor = tk.Label(self.window,
            text='Vendor',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.ink_system = tk.Label(self.window,
            text='Ink System',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.drum_weight = tk.Label(self.window,
            text='Drum Weight',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.cost = tk.Label(self.window,
            text='Cost',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.pound_cost = tk.Label(self.window,
            text='Per Pound Cost',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.reorder_point = tk.Label(self.window,
            text='Reorder Point',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.stock_warning = tk.Label(self.window,
            text='Stock Warning',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.pound_cost_value = tk.Label(self.window,
            text='Filler Text',
            font=tuple(self.fonts['notes']),
            anchor="w")
        self.lvalue = tk.Label(self.window,
            text='L',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.avalue = tk.Label(self.window,
            text='A',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.bvalue = tk.Label(self.window,
            text='B',
           font=tuple(self.fonts["label"]),
           anchor='w'
        )
        self.color_swatch = tk.Label(self.window,
            text='Color Swatch',
           font=tuple(self.fonts["label"]),
           anchor='center'
        )
        # Place Labels
        self.material_id.place(x=15, y=15, width=160, height=30)
        self.name.place(x=15, y=55, width=160, height=30)
        self.health.place(x=580, y=10, width=120, height=25)
        self.flammability.place(x=580, y=40, width=120, height=25)
        self.reactivity.place(x=580, y=70, width=120, height=25)
        self.ppe.place(x=580, y=100, width=120, height=25)
        self.description.place(x=15, y=115, width=100, height=20)
        self.comments.place(x=15, y=170, width=100, height=20)
        self.vendor.place(x=510, y=265, width=150, height=30)
        self.ink_system.place(x=510, y=295, width=150, height=30)
        self.drum_weight.place(x=510, y=325, width=150, height=30)
        self.cost.place(x=510, y=355, width=150, height=30)
        self.pound_cost.place(x=510, y=385, width=150, height=30)
        self.reorder_point.place(x=510, y=415, width=150, height=30)
        self.stock_warning.place(x=510, y=445, width=150, height=30)
        self.pound_cost_value.place(x=665, y=385, width=120, height=30)
        self.lvalue.place(x=510, y=495, width=25, height=30)
        self.avalue.place(x=510, y=530, width=25, height=30)
        self.bvalue.place(x=510, y=565, width=25, height=30)
        self.color_swatch.place(x=630, y=480, width=150, height=30)
        # Entry
        self.material_id_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.name_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.health_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.flammability_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.reactivity_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.ppe_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.description_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.vendor_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.ink_system_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.drum_weight_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.pound_cost_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.cost_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.reorder_point_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.stock_warning_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.lvalue_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.avalue_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        self.bvalue_entry = tk.Entry(self.window,
            font=tuple(self.fonts["notes"]))
        # Place Entry Widgets
        self.material_id_entry.place(x=125, y=15, width=450, height=30)
        self.name_entry.place(x=125, y=55, width=450, height=30)
        self.health_entry.place(x=705, y=10, width=75, height=25)
        self.flammability_entry.place(x=705, y=40, width=75, height=25)
        self.reactivity_entry.place(x=705, y=70, width=75, height=25)
        self.ppe_entry.place(x=705, y=100, width=75, height=25)
        self.description_entry.place(x=15, y=135, width=770, height=30)
        self.vendor_entry.place(x=665, y=265, width=120, height=30)
        self.ink_system_entry.place(x=665, y=295, width=120, height=30)
        self.drum_weight_entry.place(x=665, y=325, width=120, height=30)
        self.cost_entry.place(x=665, y=355, width=120, height=30)
        self.reorder_point_entry.place(x=665, y=415, width=120, height=30)
        self.stock_warning_entry.place(x=665, y=445, width=120, height=30)
        self.lvalue_entry.place(x=540, y=495, width=75, height=30)
        self.avalue_entry.place(x=540, y=530, width=75, height=30)
        self.bvalue_entry.place(x=540, y=565, width=75, height=30)
        # Text
        self.comment_text = tk.Text(self.window)
        self.comment_text.config(
            font=tuple(self.fonts["notes"]))
        # Place Text Widgets
        self.comment_text.place(x=15, y=190, width=770, height=70)
        # Buttons
        self.new_btn = tk.Button(self.window,
            text = 'New',
            font=tuple(self.fonts["button"]),
            command = lambda:self.mc.add())
        self.update_btn = tk.Button(self.window,
            text = 'Update',
            font=tuple(self.fonts["button"]),
            command = lambda:self.mc.update())
        self.delete_btn = tk.Button(self.window,
            text = 'Delete',
            font=tuple(self.fonts["button"]),
            command = lambda:self.mc.delete())
        self.back_btn = tk.Button(self.window,
            text = 'Back',
            font=tuple(self.fonts["button"]),
            command = lambda:self.mc.exit())
        self.update_swatch_btn = tk.Button(self.window,
            text = 'Swatch',
            font=tuple(self.fonts["button"]),
            command = lambda:self.mc.update_color(
                l=self.lvalue_entry.get(),
                a=self.avalue_entry.get(),
                b=self.bvalue_entry.get()
            )
        )
        self.update_cost_btn = tk.Button(self.window,
            text = 'Color',
            font=tuple(self.fonts["button"])
            )
        # Place Button Widgets
        self.new_btn.place(x=40, y=600, width=100, height=40)
        self.update_btn.place(x=164, y=600, width=100, height=40)
        self.delete_btn.place(x=288, y=600, width=100, height=40)
        self.back_btn.place(x=412, y=600, width=100, height=40)
        self.update_swatch_btn.place(x=536, y=600, width=100, height=40)
        self.update_cost_btn.place(x=660, y=600, width=100, height=40)

if __name__ == '__main__':
    root = tk.Tk()
    m = Materials(root)
    m.mainloop()