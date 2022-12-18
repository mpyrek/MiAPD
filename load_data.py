import numpy 
from numpy import recfromtxt
import csv

class Dataset():
    def __init__(self, datapath):
        self.headers = []
        self.rows = []
        
        with open(datapath, newline='', encoding="utf-8") as f:
            my_data = csv.reader(f)
            self.headers = next(my_data)
            for row in my_data:
                self.rows.append(row)
        
    def get_minmax_value_from_category(self, category):
        idx = self.headers.index(category)
        min_of_category = min([int(row[idx]) for row in self.rows if row[idx] != "unknown"])
        max_of_category = max([int(row[idx]) for row in self.rows if row[idx] != "unknown"])
        return (min_of_category, max_of_category)
    
    def create_dicts_array(self):
        dicts_array = []
        for row in self.rows:
            dict = {}
            for i in range(len(row)):
                if i == 0: key = "idx"
                else: key = self.headers[i]
                dict.update({ key : row[i]})
            dicts_array.append(dict)
            
        return dicts_array  
        
            
    def normalized_category(self, category):
        min_category_value, max_category_value = self.get_minmax_value_from_category(category)
        divider =  (max_category_value - min_category_value)/9
        
        # for row
    
        
        
    
# ok = Dataset('..\ski_hotels.csv')
# print(ok.headers)
# print(ok.create_dicts_array())