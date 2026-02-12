class Solution:
    def getAlternates(self, arr):
        # Code Here
        #return arr[::2]
        
        arr1 = []
        n = len(arr)
        
        for i in range(0, n, 2):
            arr1.append(arr[i])
        
        return arr1