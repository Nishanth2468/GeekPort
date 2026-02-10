class Solution:
    def largest(self, arr):
        # code here
        temp = arr[0]
        n = len(arr)
        
        for i in range(n) :
            if arr[i] > temp :
                temp = arr[i]
                
        
        return temp
