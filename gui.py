# mosty jako rozszerzenie

import tkinter as tk
import load_data
from load_data import Dataset
from tkinter import ttk



def callback(window, row, sliders, priorities):
    for slider in sliders:
        if slider.get() == 0:
            shoutout = ttk.Label(window, text='Change all criteria!')
            shoutout.grid(row=row, padx=20, pady=30, columnspan=3)
            return

    # do sth with priorities
    shoutout = ttk.Label(window, text='Change all criteria!')
    shoutout.grid(row=row, padx=20, pady=30, columnspan=3)
    slider_changed(sliders)
    
    data = [(sliders[i].get(), int(priorities[i].get())) for i in range(len(sliders))]
    print(data)
    
    
def slider_changed(sliders):
    for slider in sliders:
        print(slider.get())

def disp(val):
    print(val)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #dataset
        mydata = Dataset('ski_hotels.csv')
        
        # root window
        self.title('Skiing Hotels Decision Maker')
        self.geometry('800x600')
        self.iconbitmap("snowflake.ico")
        # self.style = ttk.Style(self)

        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "light")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # title
        title = ttk.Label(self, text='This is the best place to find your perfect skiing hotel!\n just select your preferences and click the button')
        title.grid(row=0, padx=20, pady=30, columnspan=3)

        # inpu
        criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste distance (km)", "total lifts", "total gondolas"]
        categories = ["price (£)", "distance_from_lift_(m)", "altitude (m)", "totalPiste (km)", "totalLifts", "gondolas"] 
        scales = [mydata.get_minmax_value_from_category(cat) for cat in categories]
        print(scales)
        sliders = [tk.Scale(self, from_=scales[i][0], to=scales[i][1], orient=tk.HORIZONTAL, command = disp) for i in range(len(criteria))]
        labels = [ttk.Label(self, text=t) for t in criteria]

        priorities = [ttk.Spinbox(self, from_=1, to=6, increment=1) for _ in criteria]
        for i in range(len(criteria)):
            labels[i].grid(column=0, row=i+1, padx=10, pady=10)
            sliders[i].grid(column=1, row=i+1, padx=10, pady=10)
            priorities[i].insert(0, "priority")
            priorities[i].grid(column=2, row=i+1, padx=10, pady=10)

        # button
        self.btn = ttk.Button(self, text='Calculate', command = lambda: callback(self, len(criteria)+2, sliders, priorities))
        self.btn.grid(row= len(criteria)+1, padx=10, pady=10, columnspan=3)
        

        # def change_theme(self):
        #     self.style.theme_use(self.selected_theme.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
