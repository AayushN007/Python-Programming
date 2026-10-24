class Solution:
    def alternatingSubarray(self, nums):
        max_len_alt_subarray = None
        running_len_alt_subarray = None
        
        len_nums = len(nums)

        i = 0
        while (i < len_nums):
            if (running_len_alt_subarray is not None and i >= 2 and nums[i-2] == nums[i]):
                running_len_alt_subarray += 1
            elif (i >= 1 and nums[i-1] == nums[i] - 1):
                running_len_alt_subarray = 2
            else:
                running_len_alt_subarray = None

            if ((max_len_alt_subarray is None and running_len_alt_subarray is not None) or (max_len_alt_subarray is not None and running_len_alt_subarray is not None and running_len_alt_subarray > max_len_alt_subarray)):
                max_len_alt_subarray = running_len_alt_subarray
            i += 1
        
        if (max_len_alt_subarray is not None):
            return max_len_alt_subarray
        else:
            return -1