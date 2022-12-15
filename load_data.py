import numpy 
from numpy import recfromtxt
import csv

class Dataset():
    def __init__(self, datapath):
        self.headers = []
        self.rows = []
        
        with open(datapath, newline='', encoding="utf-8") as f:
            mydata = csv.reader(f)
            self.headers = next(mydata)
            for row in mydata:
                self.rows.append(row)
        
    def get_minmax_value_from_category(self, category):
        idx = self.headers.index(category)
        minofcategory = min([int(row[idx]) for row in self.rows if row[idx] != "unknown"])
        maxofcategory = max([int(row[idx]) for row in self.rows if row[idx] != "unknown"])
        return (minofcategory, maxofcategory)
    
        
        
    
# ok = Dataset('..\ski_hotels.csv')
# print(ok.headers)
# print(ok.get_minmax_value_from_category("distance from lift (m)"))