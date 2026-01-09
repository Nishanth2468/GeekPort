# class Solution:
#     def maxPerimeter(self, arr):
#         #code here.
#         arr.sort(reverse=True)
#         High = arr[0]
#         High1 = arr[1]
#         High2 = arr[2]
        
#         if High1+High2 > High :
#             return High+High1+High2
#         else :
#             return -1
        
        
class Solution: 
    def maxPerimeter(self, arr):
        
        if len(arr) < 3:
            return -1
        
        # Sort in descending order to get maximum perimeter first
        arr.sort(reverse=True)
        
        # Here in this for loop we are Checking the consecutive triplets
        for i in range(len(arr) - 2) :
            
            a, b, c = arr[i], arr[i+1], arr[i+2]
            
            # Here we are checking the Triangle condition
            if c + b > a :
                return a+b+c
        
        return -1