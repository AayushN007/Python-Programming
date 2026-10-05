class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        j = 1  # Pointer for odd indices
        
        # Scan all even indices
        for i in range(0, n, 2):
            
            # If even index has even number, it's correct
            if nums[i] % 2 == 0:
                continue
            
            # If even index has odd number, find an even number at odd index
            while nums[j] % 2 != 0:
                j += 2
            
            # Swap: even number from odd index goes to even index
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums