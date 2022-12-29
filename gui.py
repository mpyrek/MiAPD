import tkinter as tk
from load_data import Dataset
from tkinter import DoubleVar, ttk
from RangeSlider.RangeSlider import RangeSliderH 
from AHP_matrix2 import *
from expert_page import *
from weights_page import *

def calculate(window, hotels):
    # we are calculating!
    result = hotels[get_best()]

    # view the result    
    values = window.mydata.get_values(list(result.values())[0])
    headers = tuple(result.keys())[1:4] + tuple(window.criteria)
    data = values

    result_view = ttk.Treeview( window, selectmode='none', columns=headers, height=2)    
    result_view.column('#0', anchor="center", stretch=False , width=1)
    for header in headers:
        result_view.heading(header, text=header, anchor="center")
        if header == "hotel" or len(header) > 20: result_view.column(header, anchor="center", width=150)
        else: result_view.column(header, anchor="center", width=90)
    result_view.grid(row=10, column=0, columnspan=3, pady=30)
    result_view.insert(parent='', index=0, iid=0, values=data)

def get_expert(window, category, search_range):
    search_range = [int(var) for var in search_range]
    min_lim, max_lim = search_range
    window.hotels = choose_3_hotels(window.mydata, category, min_lim, max_lim)
    chosen_3 = [window.mydata.get_values(list(window.hotels[i].values())[0]) for i in range(3)]
    expert_window = ExpertApp(window, window.criteria, window.categories, chosen_3)

def get_weights(window):
    weight_window = WeightApp(window)
    
def menu_callback(window):
    # range slider
    min_, max_ = window.scale_dicts.get(window.menu_holder.get())

    hVar1 = DoubleVar(value=min_) 
    hVar2 = DoubleVar(value=max_) 

    rs1 = RangeSliderH( window , [hVar1, hVar2], padX=15, bar_radius = 7, min_val=min_, max_val=max_,
            bar_color_inner = '#acd4fc', line_s_color= "#007fff", bar_color_outer = '#007fff', line_color = '#acd4fc', 
            bgColor = '#ffffff', digit_precision = '1.0f', valueSide = 'BOTTOM', font_family ='Yu Gothic UI', font_size = 10)
    rs1.grid(row=2, padx=20, pady=20, columnspan=3)  

    # get expert button
    expert_button = ttk.Button(window, text="Get Experts' view", command = lambda : get_expert(window, list(window.scale_dicts.keys()).index(window.menu_holder.get()) + 4, rs1.getValues()))
    expert_button.grid(row=6, padx=20, pady=10, columnspan=3)

    # get weights button
    weight_button = ttk.Button(window, text="Get weights", command = lambda : get_weights(window))
    weight_button.grid(row=7, padx=20, pady=10, columnspan=3)

    # calculation button
    # + 4 bias
    calc_button = ttk.Button(window, text='Calculate', command = lambda : calculate(window, window.hotels))
    calc_button.grid(row=8, padx=20, pady=10, columnspan=3)
    return

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #dataset
        self.mydata = Dataset('ski_hotels.csv')
        
        # root window
        self.title('Skiing Hotels Decision Maker')
        self.geometry('1200x900')
        self.iconbitmap("snowflake.ico")
    
        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "light")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # title
        title = ttk.Label(self, text='This is the best place to find your perfect skiing hotel!\n just select your preferences and click the button')
        title.grid(row=0, padx=20, pady=30, columnspan=3)

        self.criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste length (km)", "total lifts", "total gondolas"]
        self.categories = ["price (£)", "distance_from_lift_(m)", "altitude (m)", "totalPiste (km)", "totalLifts", "gondolas"] 
        self.scales = [self.mydata.get_minmax_value_from_category(cat) for cat in self.categories]
        self.scale_dicts = dict(zip(self.criteria, self.scales))
        self.hotels = []

        # option menu
        self.menu_holder = tk.StringVar(value=self.criteria[0])
        self.menu_holder.trace("w", lambda x, y, z: menu_callback(self))

        self.option_menu = ttk.OptionMenu(self, self.menu_holder, self.criteria[0], *self.criteria)
        self.option_menu.grid(row=1, padx=20, pady=10, columnspan=3)
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    
