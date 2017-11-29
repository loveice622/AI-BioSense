import tkinter as tk


class DefaultPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.canvas = tk.Canvas(self, background="black")
        self.canvas.pack(side="top", fill="both", expand=True)



