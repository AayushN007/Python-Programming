class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in '([{':
                st.append(ch)
            else:
                if not st or st[-1] != pairs[ch]:
                    return False
                st.pop()
        return len(st) == 0