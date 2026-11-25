class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a','e','i','o','u'}
        sentence = sentence.split(" ")
        for i,token in enumerate(sentence):
            if token[0].lower() in vowels:
                sentence[i] = token + 'ma' +("a"*(i+1))
            else:
                sentence[i] =  token[1:] + token[0] +'ma'+ ("a"*(i+1))
        return " ".join(sentence)
        