class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        call_data = {
            "numbers" :[2,3,4,5,6,7,8,9],
            "letters" :["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        }

        words = []
        for i in digits:
            digit = int(i)
            index = call_data["numbers"].index(digit)
            words.append(call_data["letters"][index])

        result = ['']
        for word in words:
            new_result = []
            i = 0
            while i < len(result):
                for ch in word:
                    new_result.append(result[i] + ch)
                i += 1
            result = new_result
        return result