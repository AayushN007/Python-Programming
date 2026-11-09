class Solution:
    def checkRecord(self, s: str) -> bool:

        count = 0
        i = 0
        cond = True

        while i < len(s):
            if s[i] == "A":
                count += 1

            elif s[i] == 'L':
                if i + 2 < len(s) and s[i+1] == 'L' and s[i+2] == 'L':
                    cond = False

            i += 1

        if count > 1 or cond == False:
            return False

        return True      