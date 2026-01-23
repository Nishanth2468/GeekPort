class Solution:
    def leaders(self, arr):
        # code here
        # here allways the last element will be the leader 
        n = len(arr) # the size of arr
        lead = []
        
        max_element = arr[-1]
        lead.append(max_element)
        
        for i in range(n-2, -1, -1) :
            if arr[i] >= max_element :
                max_element = arr[i]
                lead.append(max_element)
                
            
        lead.reverse()    
        return lead
        
        # for i in range(n) :
        #     is_lead = True
        #     for j in range(i+1, n) :
        #         if arr[j] > arr[i] :
        #             is_lead = False
        #             break
                
        #     if is_lead :
        #         lead.append(arr[i])
            
        # return lead
        