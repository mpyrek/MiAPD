
class AHPmatrix:
    def __init__(self, user_value_dict, priorities_dict, hotel_dict):
        self.matrix = [[0*len(user_value_dict)]*len(user_value_dict)]
        
        self.user_value_dict = user_value_dict
        self.priorities_dict = priorities_dict
        self.hotel_dict = hotel_dict
        self.create_AHPmatrix()
        self.RI = [0,0,0.58,0.9, 1.12,1.24, 1.32, 1.41, 1.45, 1.49]
    
    
    def create_AHPmatrix(self):
        
        for i in range(len(self.user_value_dict)):
            _ , user_value  =  self.user_value_dict[i]
            for j in range(len(self.hotel_dict)):
                if i == j:
                    self.matrix[i][j] = 1
                    continue
                
                _ , hotel_value  = self.hotel_dict.get(list(self.user_value_dict.keys())[i])
                 
                if hotel_value is not "unknown":
                    if user_value < hotel_value:
                        self.matrix[i][j] = 1/user_value
                        self.matrix[j][i] = user_value
                    else:
                        self.matrix[i][j] = user_value
                        self.matrix[j][i] = 1/user_value
                else:
                    self.matrix[i][j] = 1
                        
                        
    def calculate_lambdamax(self):
        priority_vector = []
        for i in range(len(self.matrix)):
            sum = 0
            for el in self.matrix[i]:
                sum += el
            priority_vector = len(self.matrix)*sum
        
        lambdamax = sum([priority_vector[i]*self.priorities_dict.get(self.user_value_dict.keys()[i]) for i in range(len(priority_vector))])
        return lambdamax          
    
    
    def calculate_CI(self):
        return (self.calculate_lambdamax - len(self.matrix))/ (len(self.matrix) -1)
    
                    
    def calculate_CR(self):
        return self.calculate_CI/ self.RI[Math.randint(0, 9)]
        