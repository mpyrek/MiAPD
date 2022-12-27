import random
from load_data import Dataset
from enum_1 import Criteria
from numpy import matmul , argmax
import pandas as pd

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
    
    if n > 3:
        ids = random.sample(ids, 3)

    # print(ids)
   
    for idx in ids:
        hotels.append(data.get_dicts_array()[idx])
        
    return hotels



def get_best(hotels):
    six_matrix_criteria = create_matrix(hotels)
    priority_vextors = []
    for  i in range(len(Criteria)):
        priority_vextors.append(calculate_priority_vector(six_matrix_criteria[i]))
        
    c12_matrix = calculate_priority_vector(crate_matrix_c12())
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
        
    
def crate_matrix_c12():
    matrixc12 = []
    
    for i in range(6):
        matrixc12.append([])
        for j in range(6):
            if i != j:
                if i < j :
                    matrixc12[i].append(random.randint(2,9))
                else:
                    matrixc12[i].append( 1 / matrixc12[j][i])
            else:
                matrixc12[i].append( 1)
                
    return matrixc12
            
    

def calculate_priority_vector(matrix):
    
    sum_matrix = sum(sum(matrix,[]))
    vector = []
    for row in matrix:
        vector.append(sum(row)/ sum_matrix)
    return vector

def create_matrix(hotels):
    all_matrix = []
    for criterion in Criteria:
        # print([hotel.get(criterion.get_origin_name()) for hotel in hotels])
        all_matrix.append(cratate_matrix_for_criteria([hotel.get(criterion.get_origin_name()) for hotel in hotels]))
    return all_matrix

def cratate_matrix_for_criteria(hotels_criterion_value):
    matrix = []
    for i in range(len(hotels_criterion_value)):
        matrix.append([])
        for j in range(len(hotels_criterion_value)):
            matrix[i].append([])
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = hotels_criterion_value[i]/hotels_criterion_value[j]
    return matrix
            
    




# if __name__ == "__main__":
#     data = Dataset('..\ski_hotels.csv')
#     hotels = draw_three_hotels(data)
#     print(hotels[get_best(hotels)])