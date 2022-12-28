import tkinter as tk
from load_data import Dataset
from tkinter import ttk, IntVar 
from AHP_matrix2 import *

def get_expert_values(window):
    return

class WeightApp(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)

        #dataset
        self.mydata = Dataset('ski_hotels.csv')
        
        # root window
        self.title('Skiing Hotels Decision Maker')
        self.geometry('800x600')
        self.iconbitmap("snowflake.ico")
    
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        for i in range(7): self.rowconfigure(i, weight=1)
        
        # title
        title = ttk.Label(self, text="This is weight choosing page")
        title.grid(row=0, padx=20, pady=30, columnspan=3)

        criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste distance (km)", "total lifts", "total gondolas"]
        self.categories = ["price (£)", "distance_from_lift_(m)", "altitude (m)", "totalPiste (km)", "totalLifts", "gondolas"] 
        scales = [self.mydata.get_minmax_value_from_category(cat) for cat in self.categories]
        self.scale_dicts = dict(zip(criteria, scales))

        saaty_scale = list (range(9, 1, -1)) + list(range(1, 10))

        criteria_pairs = [(criteria[i], criteria[j]) for i in range(len(criteria)) for j in range(len(criteria)) if j > i]
        
        self.radio_frame = ttk.LabelFrame(self, text="Weights")

        self.saaty_scales = [ttk.Label(self.radio_frame, text=str(saaty)) if saaty%2 == 1 else ttk.Label(self.radio_frame, text="") for saaty in saaty_scale]

        self.criteria_labels = [(ttk.Label(self.radio_frame, text=criteria_pairs[i][0]), ttk.Label(self.radio_frame, text=criteria_pairs[i][1])) for i in range(len(criteria_pairs))] 
        
        self.groups = [IntVar(value=0) for _ in range(len(criteria_pairs))]

        self.radio_buttons = [ [ ttk.Radiobutton(self.radio_frame, value=j, variable=self.groups[i]) for j in range(len(saaty_scale)) ] for i in range(len(criteria_pairs))]

        for i in range(5):
            self.radio_frame.columnconfigure(i, weight=0)
            self.radio_frame.rowconfigure(i, weight=0)

        for i in range(len(criteria_pairs)):
            self.criteria_labels[i][0].grid(row=i, column=0)
            self.criteria_labels[i][1].grid(row=i, column=len(saaty_scale)+1)

            for k in range(len(saaty_scale)):
                self.radio_buttons[i][k].grid(row=i, column=k+1, padx=5, pady=2)

        for k in range(len(saaty_scale)): self.saaty_scales[k].grid(row=len(criteria_pairs)+1, column=k+1)

        self.radio_frame.grid(row=1, column=0)
        

    
