class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for ch in s:
            if len(st) == 0 or abs(ord(ch) - ord(st[-1])) != 32:
                st.append(ch)
            else:
                st.pop()
            
        return "".join(st)

        