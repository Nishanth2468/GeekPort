class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        # temp = [0] * n
        j = 0

        for i in range(n):
            if arr[i] != 0:
                # temp[j] = arr[i]
                arr[j], arr[i] = arr[i], arr[j]
                j += 1

        return arr
