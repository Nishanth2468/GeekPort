#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        
        if date % 2 == 0:
            fine_count = 0
            
            for i in range(len(car)) :
                if car[i] % 2 != 0 :
                    
                    fine_count += fine[i]
            
            return fine_count
        
        else :
            fine_count = 0
            
            for i in range(len(car)) :
                if car[i] % 2 == 0 :
                    
                    fine_count += fine[i]
                    
            return fine_count