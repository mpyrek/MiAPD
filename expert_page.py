import tkinter as tk
from load_data import Dataset
from tkinter import ttk, IntVar 
from AHP_matrix2 import *


class ExpertApp(tk.Toplevel):
    def __init__(self, window, criteria, categories, hotels):
        super().__init__(window)

        #dataset
        self.mydata = Dataset('ski_hotels.csv')
        
        # root window
        self.title('Skiing Hotels Decision Maker')
        self.geometry('1200x900')
        self.iconbitmap("snowflake.ico")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        for i in range(10): self.rowconfigure(i, weight=1)
        
        # title
        title = ttk.Label(self, text="This is the Expert's page")
        title.grid(row=0, column = 0, padx=20, pady=30, columnspan=3)

        headers = ("hotel",) + tuple(window.hotels[0].keys())[1:10]
        values = [] 
        for i in range(len(hotels)): values.append(("hotel "+ str(i+1),) + tuple(hotels[i])) 

        tree = ttk.Treeview( self, selectmode='none', columns=headers, height=2)    
        tree.column('#0', anchor="center", stretch=False , width=1)
        for header in headers:
            tree.heading(header, text=header, anchor="center")
            if header == "hotel" or len(header) > 20 or header == "resort": tree.column(header, anchor="center", width=150)
            else: tree.column(header, anchor="center", width=90)

        for i in range(len(values)):
            tree.insert(parent='', index=i, iid=i, values=values[i])

        tree.grid(row=0, column=0, columnspan=3, pady=5)

        criteria = ["price (£)", "distance from lift (m)", "altitude (m)", "total piste distance (km)", "total lifts", "total gondolas"]
        self.categories = ["price (£)", "distance_from_lift_(m)", "altitude (m)", "totalPiste (km)", "totalLifts", "gondolas"] 
        scales = [self.mydata.get_minmax_value_from_category(cat) for cat in self.categories]
        self.scale_dicts = dict(zip(criteria, scales))

        saaty_scale = list (range(9, 1, -1)) + list(range(1, 10))

        hotel_names = [("hotel 1", "hotel 2"), ("hotel 2", "hotel 3"), ("hotel 1", "hotel 3")]

        self.radio_frames = [ ttk.LabelFrame(self, text=cri) for cri in criteria ]

        self.saaty_scales = [[ttk.Label(self.radio_frames[i], text=str(saaty), font=("Segoe Ui", 8)) 
                            if saaty%2 == 1 else ttk.Label(self.radio_frames[i], text="") for saaty in saaty_scale] for i in range(len(criteria)) ]

        self.hotel_labels = [[(ttk.Label(self.radio_frames[j], text=hotel_names[i][0]), 
                            ttk.Label(self.radio_frames[j], text=hotel_names[i][1])) for i in range(len(hotel_names))] for j in range(len(criteria))]
        
        self.groups = [[IntVar(value=0) for _ in range(3)] for _ in range(len(criteria)) ]

        self.radio_buttons = [ [ [ ttk.Radiobutton(self.radio_frames[k], value=j, variable=self.groups[k][i], padding=(2, 2)) for j in range(len(saaty_scale)) ] for i in range(3)] for k in range(len(criteria))]
        
        self.button = ttk.Button(self, text="Done!",command = lambda : self.get_expert_values(criteria, self.groups )).grid(row=3,pady = 1, column = 1)
        
        self.results_arrays =  [ [[1 for i in range(3)] for i in range(3)] for i in range(len(criteria))]
        
         # for every radio_frame
        for i in range(len(criteria)):

            for j in range(6):
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

            self.radio_frames[i].grid(row=i+1, column=0)
            
    def get_expert_values(self, criteria, groups):
        
        for k in range(len(criteria)):
            for j in range(3):
                res = self.scale_value(0)
                if groups[k][j].get():
                    res = self.scale_value(groups[k][j].get())
                
                match j:
                    case 0:
                        self.results_arrays[k][0][1] = res
                        self.results_arrays[k][1][0] = 1/res
                    case 1:
                        self.results_arrays[k][1][2] = res
                        self.results_arrays[k][2][1] = 1/res
                    case 2:
                        self.results_arrays[k][0][2] = res
                        self.results_arrays[k][2][0] = 1/res
        
        change_array(self.results_arrays)                
        self.destroy()
        
    def get_arrays(self):
        return self.results_arrays
                
    def scale_value(self, arg):
        if arg  <= 8:
            return 1 / ( 9 - arg) 
        else:
            return arg - 8
                
    
