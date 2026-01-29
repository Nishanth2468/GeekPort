class Solution:
    def search(self, arr, x):
        # code here
        n = len(arr)
        
        for num in range(n) :
            if arr[num] == x :
                return num
                
        return -1
            