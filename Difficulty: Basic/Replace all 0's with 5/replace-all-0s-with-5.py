# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        
        # return int(str(n).replace('0', '5'))
        # 1004 (int)
        #  ↓ str()
        # "1004"
        #  ↓ replace('0','5')
        # "1554"
        # ↓ int()
        # 1554
        
        # Convert the integer number into a string
        # This allows us to access each digit using indexing
        tmp = str(n)
        
        # Initialize an empty string to store the result
        res = ""
        
        # Loop through each character (digit) in the string
        for i in range(len(tmp)):
            
            # If the current digit is '0'
            if tmp[i] == "0":
                # Replace '0' with '5' and add it to result
                res += "5"
            else:
                # Otherwise, add the original digit to result
                res += tmp[i]
        
        # Convert the final string back to integer and return it
        return int(res)
