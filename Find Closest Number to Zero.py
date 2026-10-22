class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]
        mindis = abs(nums[0])

        for num in nums:
            a = abs(num)

            # Update if closer, or pick the positive twin on tie
            if a < mindis or (a == mindis and num > closest):
                closest = num
                mindis = a

        return closest