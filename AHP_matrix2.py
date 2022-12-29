import random
from load_data import Dataset
from enum_1 import Criteria
from numpy import matmul , argmax
import pandas as pd

def change_importace(arr):
    global arr_importance
    arr_importance = arr
    
    
def change_array(arr):
    global arr_criteria
    arr_criteria = arr


def draw_three_hotels(data):
    three_hotels = []
    three_idx = []
    
    while(len(three_idx) < 3):
        idx = random.randint(1, 120)
        if idx not in three_idx:
            three_idx.append(idx)
            
    for idx in three_idx:
        three_hotels.append(data.get_dicts_array()[idx])
        
    return three_hotels


def choose_3_hotels(data, criterion, min_lim, max_lim):
    hotels = []
    ids = []

    filtered_data =  [d for d in data.rows if int(d[criterion]) >= min_lim and int(d[criterion]) <= max_lim]
    ids = [int(f[0]) for f in filtered_data]
    n = len(ids)

    while n < 3:
        idx = random.randint(1, 120)
        if idx not in ids:
            ids.append(idx)
            n += 1
    
    if n > 3: ids = random.sample(ids, 3)

    for idx in ids:
        hotels.append(data.get_dicts_array()[idx])
    
    return hotels


def get_best():
    priority_vextors = []
    for  i in range(len(Criteria)):
        priority_vextors.append(calculate_priority_vector(arr_criteria[i]))
        
    c12_matrix = calculate_priority_vector(arr_importance)
    matrix_all_weights = paste_all_weights_matrix(priority_vextors)
    res = matmul(matrix_all_weights , c12_matrix)
    
    return argmax(res)
    
    
def paste_all_weights_matrix(matrix_p):
    matrix_all_weights = []
    
    for j in range(3):
        matrix_all_weights.append([])
        for i in range(len(Criteria)):
            matrix_all_weights[j].append(matrix_p[i][j])
    
    return matrix_all_weights
        
            
def calculate_priority_vector(matrix):
    
    sum_matrix = sum(sum(matrix,[]))
    vector = []
    for row in matrix:
        vector.append(sum(row)/ sum_matrix)
    return vector
