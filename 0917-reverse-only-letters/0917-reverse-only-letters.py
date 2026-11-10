class Solution:
    def reverseOnlyLetters(self, s):

        letters = [ch for ch in s if ch.isalpha()]
        letters.reverse()

        result = []
        index = 0

        for ch in s:

            if ch.isalpha():
                result.append(letters[index])
                index += 1
            else:
                result.append(ch)

        return ''.join(result)