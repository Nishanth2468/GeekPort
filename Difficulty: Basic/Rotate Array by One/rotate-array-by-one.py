#User function Template for python3
class Solution:
    def rotate(self, arr):
        # code
        # This is using sclicing
        # arr = [arr[-1]] + arr[:-1]
        
        # This is using with pop and insert function
        # last = arr.pop()
        # arr.insert(0, last)
        
        # return arr
        
        # In-place rotation method
        n = len(arr)
        
        last = arr[-1]
        
        for i in range(n-1, 0, -1) :
            arr[i] = arr[i-1]
        
        arr[0] = last 
        
        return arr