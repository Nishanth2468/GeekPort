class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        # we will only check the elements txt - pat exaple txt is 20 and pat is 3 then we will only check till 20-3 = 17th index
        # the comparition will be of for pat =3 will be (0,2)-(1,3)-(2,4)-(3,5)
        # so it will be i+len(pat) = (0, 3) in strings
        
        n = len(txt)
        m = len(pat)
        
        for i in range(n - m + 1) :
            size = i
            if txt[i:m+i] == pat:
                return size
        
        return -1
        
        