class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        output = []
        words = s.split(' ')
        for i in range(k):
            output.append(words[i])
        return ' '.join(output)
