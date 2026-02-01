#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TuxPad:
    def __init__(self, root):
        self.root = root
        self.root.title("TuxPad 0.0 Core")
        self.root.geometry("900x750")
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
            if os.path.exists(icon_path):
                img = tk.PhotoImage(file=icon_path)
                self.root.iconphoto(False, img)
        except Exception:
            pass

        
        self.header_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.header_frame.pack(fill="x", side="top", padx=10, pady=5)
        self.title_label = tk.Label(self.header_frame, text="🐧 TuxPad 0.0 Core", 
                                    font=("Segoe UI", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(side="left")

        
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")

        # Using standard fixed fonts: Consolas for Windows, Courier for others
        font_choice = ("Consolas", 12) if os.name == 'nt' else ("Courier", 12)
        
        self.text_area = tk.Text(self.root, undo=True, font=font_choice,
                                 yscrollcommand=self.scrollbar.set, 
                                 padx=10, pady=10, borderwidth=0)
        self.text_area.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.text_area.yview)

        
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y")

        
        self.root.bind_all('<Control-n>', lambda e: self.new_file())
        self.root.bind_all('<Control-o>', lambda e: self.open_file())
        self.root.bind_all('<Control-s>', lambda e: self.save_file())


if __name__ == "__main__":
    root = tk.Tk()
    app = TuxPad(root)
    root.mainloop()

