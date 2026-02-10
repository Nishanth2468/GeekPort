class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        arr1 = sorted(a)
        arr2 = sorted(b)
        
        if arr1 == arr2 :
            return True
        else :
            return False