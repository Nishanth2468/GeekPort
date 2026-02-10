#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        # reverse = ""
        
        # for ch in s:
        #     reverse = ch + reverse
            
        # return reverse
        
        # OR we can use Slicing
        
        reverse = s[::-1]
        
        return reverse