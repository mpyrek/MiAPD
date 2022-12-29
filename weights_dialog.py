import tkinter as tk
from load_data import Dataset
from tkinter import ttk, IntVar 
from AHP_matrix2 import *

class WeightApp(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)

        #dataset
        self.mydata = Dataset('ski_hotels.csv')
        
        # root window
        self.title('Skiing Hotels Decision Maker')
        self.geometry('1200x900')
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

        self.button = ttk.Button(self, text="Done!",command = lambda : self.get_expert_values(criteria_pairs, self.groups )).grid(row=3,pady = 2, column = 1)
        
        self.importance_criteria_array = [[1 for i in range(len(criteria))] for j in range(len(criteria))]
        
        
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
        
    
    def get_expert_values(self, criteria, groups):
        
        for k in range(len(criteria)):
                res = self.scale_value(0)
                if groups[k].get():
                    res = self.scale_value(groups[k].get())
                match k:
                    case 0:
                        self.importance_criteria_array[0][1] = res
                        self.importance_criteria_array[1][0] = 1/res
                    case 1:
                        self.importance_criteria_array[0][2] = res
                        self.importance_criteria_array[2][0] = 1/res
                    case 2:
                        self.importance_criteria_array[0][3] = res
                        self.importance_criteria_array[3][0] = 1/res   
                    case 3:
                        self.importance_criteria_array[0][4] = res
                        self.importance_criteria_array[4][0] = 1/res   
                    case 4:
                        self.importance_criteria_array[0][5] = res
                        self.importance_criteria_array[5][0] = 1/res   
                    case 5:
                        self.importance_criteria_array[1][2] = res
                        self.importance_criteria_array[2][1] = 1/res 
                    case 6:
                        self.importance_criteria_array[1][3] = res
                        self.importance_criteria_array[3][1] = 1/res 
                    case 7:
                        self.importance_criteria_array[1][4] = res
                        self.importance_criteria_array[4][1] = 1/res
                    case 8:
                        self.importance_criteria_array[1][5] = res
                        self.importance_criteria_array[5][1] = 1/res
                    case 9:
                        self.importance_criteria_array[2][3] = res
                        self.importance_criteria_array[3][2] = 1/res 
                    case 10:
                        self.importance_criteria_array[2][4] = res
                        self.importance_criteria_array[4][2] = 1/res
                    case 11:
                        self.importance_criteria_array[2][5] = res
                        self.importance_criteria_array[5][2] = 1/res
                    case 12:
                        self.importance_criteria_array[3][4] = res
                        self.importance_criteria_array[4][3] = 1/res
                    case 13:
                        self.importance_criteria_array[3][5] = res
                        self.importance_criteria_array[5][3] = 1/res
                    case 14:
                        self.importance_criteria_array[4][5] = res
                        self.importance_criteria_array[5][4] = 1/res  
        
        change_importace(self.importance_criteria_array)
        self.destroy()
                
                
    def scale_value(self, arg):
        if arg  <= 8:
            return 1 / ( 9 - arg) 
        else:
            return arg - 8
        
    def get_importance_arrays(self):
        return self.importance_criteria_array
    

    
