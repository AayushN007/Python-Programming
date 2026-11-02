class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        return '-'.join(map(''.join,batched(re.sub('-','',s).upper()[::-1],k)))[::-1]