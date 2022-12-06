# mosty jako rozszerzenie

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Skiing Hotels Decision Maker')
        self.geometry('800x600')
        self.iconbitmap("snowflake.ico")
        #self.style = ttk.Style(self)

        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "light")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # title
        title = ttk.Label(self, text='This is the best place to find your perfect skiing hotel')
        title.grid(row=0, padx=20, pady=30, columnspan=2)

        criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste distance (km)", "total lifts", "total gondolas"]
        scales = [(), (), (), (), (), ()]
        
        sliders = [ttk.Scale(self, from_=0, to=200, orient=tk.HORIZONTAL) for _ in criteria]
        labels = [ttk.Label(self, text=t) for t in criteria]

        for i in range(len(criteria)):
            labels[i].grid(column=0, row=i+1, padx=10, pady=10)
            sliders[i].grid(column=1, row=i+1, padx=10, pady=10)

        # # button
        # btn = ttk.Button(self, text='Show')
        # btn.grid(column=1, row=1, padx=10, pady=10)

        # def change_theme(self):
        #     self.style.theme_use(self.selected_theme.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
