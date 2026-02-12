# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    # for num in arr :
    #     if str(num) != str(num)[::-1] :
    #         return False
            
    # return True
    
    for num in arr:
        original = num
        rev = 0

        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10

        if original != rev:
            return False

    return True
    
    