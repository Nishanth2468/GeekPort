class Solution:
    def findDuplicates(self, arr):
        # code here
        # n = len(arr)
        # duplicates = []
        # # count = 0
        
        # for i in range(n) :
        #     for j in range(i + 1, n) :
        #         if arr[i] == arr[j] :
        #             duplicates.append(arr[i])
                               
        # return duplecate

        
        # Approach 2
        # duplicates = []
        # freq = {}
        
        # for num in arr :
        #     freq[num] = freq.get(num, 0) + 1
            
        # for key in freq :
        #     if freq[key] > 1 :
        #         duplicates.append(key)
                
        # return duplicates

        # This approach 3 is really good
        # res = []
        # for i in range(len(arr)):
        #     idx = abs(arr[i]) - 1
                    
        #     if arr[idx] < 0:
        #         res.append(abs(arr[i]))
        #     else:
        #         arr[idx] = -arr[idx]
        
        # return res

        # Approach 4:
        seen = set()
        duplicates = []
        
        for i in arr :
            if i in seen :
                # if i not in duplicates: to avoid repeating duplicates
                duplicates.append(i)
            else :
                seen.add(i)
                    
        return duplicates
        
        
