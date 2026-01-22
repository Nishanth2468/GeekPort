class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first = second = float('-inf')
        
        for i in arr :
            if i > first :
                second = first
                first = i
            elif first > i > second :
                second = i
            # else :
            #     return -1
            
        if second == float('-inf') :
            return -1
        else :
            return second
        