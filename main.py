import tkinter as tk
from DefaultPage import *

if __name__ == "__main__":
    root = tk.Tk()
    DefaultPage(root).pack(side="top", fill="both", expand=True)
    root.mainloop()