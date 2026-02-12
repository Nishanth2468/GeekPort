
from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        n = len(arr)
        
        for i in range(n):
            size = i+1
            if arr[i] == k:
                return size
                break
        
        return -1
        
