class Solution:
    def checkIfExist(self, arr):
        n = len(arr)

        for i in range(n):
            target = arr[i] * 2

            for j in range(n):
                if arr[j] == target and i != j:
                    return True

        return False