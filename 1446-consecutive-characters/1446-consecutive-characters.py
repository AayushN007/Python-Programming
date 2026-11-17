class Solution:
    def maxPower(self, s: str) -> int:
        return max(len([*g]) for _,g in groupby(s))