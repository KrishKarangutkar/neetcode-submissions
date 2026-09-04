class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        empty = False
        new_word = ""
        while not empty:
            if len(word1) > 0:
                new_word += word1[0:1]
                word1 = word1[1:]
            if len(word2) > 0:
                new_word += word2[0:1]
                word2 = word2[1:]
            if (len(word1)==0 and len(word2)==0):
                empty = True
        return new_word