class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)

        def place(idx, dots):
            if dots == 0 and idx == n:
                return [""]
            elif dots == 0 or idx == n:
                return []

            if s[idx] == "0":
                if idx == 0:
                    suffix = "0"
                else:
                    suffix = ".0"

                return [suffix + partial for partial in place(idx+1, dots -1)]
            else:
                res = []
                for size in range(1, min(3, n-idx) + 1):
                    num = int(s[idx:idx+size])
                    if num < 256:
                        rest = place(idx+size, dots-1)
                        if idx == 0:
                            suffix = s[idx:idx+size]
                        else:
                            suffix = "." + s[idx:idx+size]
                        res += [suffix + partial for partial in rest]

                return res
        return place(0, 4)