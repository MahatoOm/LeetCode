class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        m = len(word1)
        n = len(word2)
        res = ''
        for x, y in zip(word1, word2):
            # print(x,y)

            res += x
            res += y

            # print(res) 

        if m > n:
            res += word1[-(m-n):]
        if n > m:
            res += word2[-(n-m):]

        return res