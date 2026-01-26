class Solution:
    def findDuplicates(self, arr):
        # code here
        # n = len(arr)
        # duplecate = []
        # # count = 0
        
        # for i in range(n) :
        #     for j in range(i + 1, n) :
        #         if arr[i] == arr[j] :
        #             duplecate.append(arr[i])
                    
                    
        # return duplecate
        
        seen = set()
        duplecates = []
        
        for i in arr :
            if i in seen :
                duplecates.append(i)
            else :
                seen.add(i)
                    
        return duplecates
        
        