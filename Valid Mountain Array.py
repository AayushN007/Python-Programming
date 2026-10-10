class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr)<3:
            return False
        
        if arr==sorted(arr):
            return False
        i=0 
        while i+1<len(arr) and arr[i]<arr[i+1]:
            i+=1
        if i==0 or i==len(arr):
            return False
        while i+1<len(arr) and arr[i]>arr[i+1]:
            i+=1
        return i==len(arr)-1
        