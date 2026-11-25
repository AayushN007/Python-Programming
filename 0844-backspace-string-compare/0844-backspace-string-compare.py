class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            s_str = ""
            for i in range(len(s)):
                if s[i] == "#":
                    s_str = s_str[:-1]
                    continue
                s_str =s_str +s[i]
            return s_str
        return helper(s) ==helper(t)
        