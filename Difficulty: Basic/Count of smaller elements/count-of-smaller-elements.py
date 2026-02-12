#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        n = len(arr)
        
        count = 0
        
        for i in range(n) :
            if arr[i] <= x:
                count += 1
                
        return count

