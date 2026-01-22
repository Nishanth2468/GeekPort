class Solution:
    def canServe(self, arr):
        # code here 
        # in the arr[i] = [5,5,10,20] the total sum is 40%10 is 0 so this will be false
        # in the arr[i] = [5,5,5,10,20] the total sum is 45%10 is 5 so we have 5 coins left so ture 
        #n = int(input())
        #arr = list(map(int, input().split()))
        # There are only 5, 10, 20 notes in the array
        
        # sum = 0
        
        # for i in range(len(arr)) :
        #     sum = sum + arr[i]
        
        # if sum%10 == 0 :
        #     return False
        # else :
        #     return True
        
        # 1. Assume three counters to keep track of ₹5, ₹10, and ₹20 notes.

        # 2. Traverse the array one payment at a time.

        # 3. If the element is 5, increase the count of ₹5 notes.

        # 4. If the element is 10, check if count of ₹5 is greater than 0; if not, return false, otherwise give one ₹5 as change.

        # 5. If the element is 20, first try to give one ₹10 and one ₹5 as change; if not possible, try three ₹5 notes, else return false.
        
        
        count_five = 0
        
        count_ten = 0
        
        for bill in arr :
            if bill == 5:
                count_five += 1 # if there is only 5 no change required.
            
            elif bill == 10 :
                if count_five <= 0 :
                    return False # if there is a 10 note and no 5 notes then we return false
                else :
                    count_five -= 1
                    count_ten += 1 
            
            else :
                if count_five > 0 and count_ten > 0:
                    count_ten -= 1
                    count_five -= 1
                elif count_five >= 3 :
                    count_five -= 3
                else :
                    return False
        
        return True
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                