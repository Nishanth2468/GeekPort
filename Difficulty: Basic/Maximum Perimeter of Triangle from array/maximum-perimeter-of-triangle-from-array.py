class Solution:
    def maxPerimeter(self, arr):
        #code here.
        arr.sort(reverse=True)
        High = arr[0]
        High1 = arr[1]
        High2 = arr[2]
        
        if High1+High2 > High :
            return High+High1+High2
        else :
            return -1
        