class Solution:
    def missingNum(self, arr):
        # code here
        arr.sort()
        found = -1
        
        for x in range(len(arr)) :
            element = x + 1
            
            if arr[x] != element :
                found = element
                break
        if found == -1:
            found = len(arr) + 1
            
        return found