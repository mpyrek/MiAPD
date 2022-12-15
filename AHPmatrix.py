
class AHPmatrix:
    #get normalized vectors 1-10
    def __init__(self, uservaluedict, prioritiesdict, hoteldict):
        self.matrix = [[0*len(uservaluedict)]*len(uservaluedict)]
        self.uservaluedict = uservaluedict
        self.prioritiesdict = prioritiesdict
        self.hoteldict = hoteldict
        
        
    def create_AHPmatrix(self, valuecategory):
        
        for i in range(len(self.uservaluedict)):
            _, uservalue  =  self.uservaluedict[i]
            for j in range(len(self.hoteldict)):
                if i == j:
                    self.matrix[i][j] = 1
                    continue
                
                _, hotelvalue  = self.hoteldict[j]
                if hotelvalue is not "unknown":
                    if uservalue < hotelvalue:
                        self.matrix[i][j] = 1/uservalue
                        self.matrix[j][i] = uservalue
                    else:
                        self.matrix[i][j] = uservalue
                        self.matrix[j][i] = 1/uservalue
                else:
                    self.matrix[i][j] = 1
                        
                        
    def calculatelambdamax(self):
        priorityvector = []
        for i in range(len(self.matrix)):
            sum = 0
            for el in self.matrix[i]:
                sum += el
            priorityvector = len(self.matrix)*sum
        
        lambdamax = sum([priorityvector[i]*self.prioritiesdict.get(self.uservaluedict.keys()[i]) for i in range(len(priority_vector))])
        return lambdamax          
                    
                        
            