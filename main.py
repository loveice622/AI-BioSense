from stdlib import *
from StartPage import *

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container=tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}

        for f in (StartPage,LoadPage):
            frame=f(container,self)
            self.frames[f]=frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()