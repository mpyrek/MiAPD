import tkinter as tk
from load_data import Dataset
from tkinter import ttk, IntVar 
from AHP_matrix2 import *

def get_expert_values(window):
    return

class ExpertApp(tk.Toplevel):
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
        title = ttk.Label(self, text="This is the Expert's page")
        title.grid(row=0, padx=20, pady=30, columnspan=3)

        criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste distance (km)", "total lifts", "total gondolas"]
        self.categories = ["price (£)", "distance_from_lift_(m)", "altitude (m)", "totalPiste (km)", "totalLifts", "gondolas"] 
        scales = [self.mydata.get_minmax_value_from_category(cat) for cat in self.categories]
        self.scale_dicts = dict(zip(criteria, scales))

        saaty_scale = list (range(9, 1, -1)) + list(range(1, 10))
        hotels = [("hotel 1", "hotel 2"), ("hotel 2", "hotel 3"), ("hotel 1", "hotel 3")]

        self.radio_frames = [ ttk.LabelFrame(self, text=cri) for cri in criteria ]

        self.saaty_scales = [[ttk.Label(self.radio_frames[i], text=str(saaty)) if saaty%2 == 1 else ttk.Label(self.radio_frames[i], text="") for saaty in saaty_scale] for i in range(len(criteria)) ]

        self.hotel_labels = [[(ttk.Label(self.radio_frames[j], text=hotels[i][0]), ttk.Label(self.radio_frames[j], text=hotels[i][1])) for i in range(len(hotels))] for j in range(len(criteria))]
        
        self.groups = [[IntVar(value=0) for _ in range(3)] for _ in range(len(criteria)) ]

        self.radio_buttons = [ [ [ ttk.Radiobutton(self.radio_frames[k], value=j, variable=self.groups[k][i]) for j in range(len(saaty_scale)) ] for i in range(3)] for k in range(len(criteria))]

        # for every radio_frame
        for i in range(len(criteria)):

            for j in range(5):
                self.radio_frames[i].columnconfigure(j, weight=0)
                self.radio_frames[i].rowconfigure(j, weight=0)

            # for every comparison
            for j in range(3):
                self.hotel_labels[i][j][0].grid(row=j, column=0)
                self.hotel_labels[i][j][1].grid(row=j, column=len(saaty_scale)+1)

                # for every scale number
                for k in range(len(saaty_scale)):
                    self.radio_buttons[i][j][k].grid(row=j, column=k+1, padx=5, pady=2)

            for k in range(len(saaty_scale)): self.saaty_scales[i][k].grid(row=4, column=k+1)

            self.radio_frames[i].grid(row=i, column=0)

        
if __name__ == "__main__":
    app = ExpertApp()
    app.mainloop()
    
