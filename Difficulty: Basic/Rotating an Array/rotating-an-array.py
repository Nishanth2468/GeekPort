#User function Template for python3

class Solution:
    def leftRotate(self, arr, d):
        # code here
        n = len(arr)
        arr1 = [0] * n
        
        for i in range(n) :
            arr1[i] = arr[(i + d) % n]
        
        for i in range(n) :
            arr[i] = arr1[i]
            
        