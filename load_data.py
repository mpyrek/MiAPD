import numpy 
from numpy import recfromtxt
import csv
from enum_1 import Criteria

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
        idx_of_category = self.headers.index(category)
        min_of_category = min([int(row[idx_of_category]) for row in self.rows if row[idx_of_category] != "unknown"])
        max_of_category = max([int(row[idx_of_category]) for row in self.rows if row[idx_of_category] != "unknown"])
        return (min_of_category, max_of_category)
    
    def create_dicts_array(self):
        for criteria in Criteria:
            self.normalize_category(criteria)
        
        dicts_array = []
        for row in self.rows:
            dict = {}
            for i in range(len(row)):
                if i == 0: key = "idx"
                else: key = self.headers[i]
                dict.update({ key : row[i]})
            dicts_array.append(dict)
            
        return dicts_array  
        
            
    def normalize_category(self, category):
        min_category_value, max_category_value = self.get_minmax_value_from_category(category)
        divider =  (max_category_value - min_category_value)/9
        
        idx = self.headers.index(category)
        
        for i in range(len(self.rows)):
            if self.rows[i][idx] != 'unknown': self.rows[i][idx] = (int(self.rows[i][idx]) - min_category_value)/divider
            else: self.rows[i][idx] = 4
            
    
    def normalize_value(self, category, value):
        min_category_value, max_category_value = self.get_minmax_value_from_category(category)
        divider =  (max_category_value - min_category_value)/9
        
        return (value - min_category_value)/divider

        
        
    
# ok = Dataset('..\ski_hotels.csv')
# print(ok.headers)
# print(ok.create_dicts_array())
# print(ok.normalized_category("febSnowHigh2020(cm)"))