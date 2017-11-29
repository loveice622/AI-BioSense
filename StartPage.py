from stdlib import *


class StartPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(LoadPage))
        button1.pack()


class LoadPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="BackHome",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
