class Solution:
    def valueEqualToIndex(self, arr):
        # code:
        # lets take a array of size 5 0-4 index right so
        # we check if there is a element in a array which is less that or equal to the size of arr
        
        n = len(arr)
        
        arr1 = []
        
        for i in range(n):
            size = i+1
            if size == arr[i]:
                arr1.append(arr[i])
        
        return arr1