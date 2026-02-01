#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox

class TuxPadLite:
    def __init__(self, root):
        self.root = root
        self.root.title("TuxPad Lite")
        
        # Standard Linux monospace font
        self.text_area = tk.Text(self.root, undo=True, font=("Monospace", 11), borderwidth=0)
        self.scrollbar = tk.Scrollbar(self.root, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.pack(expand=True, fill="both")

        # Minimal Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        file_m = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_m)
        file_m.add_command(label="New", command=self.new_f)
        file_m.add_command(label="Open", command=self.open_f)
        file_m.add_command(label="Save", command=self.save_f)
        file_m.add_separator()
        file_m.add_command(label="Exit", command=root.destroy)

    def new_f(self):
        self.text_area.delete(1.0, tk.END)

    def open_f(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())

    def save_f(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    TuxPadLite(root)
    root.mainloop()

