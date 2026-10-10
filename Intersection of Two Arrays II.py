class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}
        for element in nums1:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1    
        result = []        
        for element in nums2:
            if element in freq and freq[element] > 0:
                 result.append(element)
                 freq[element] -= 1
        return result         