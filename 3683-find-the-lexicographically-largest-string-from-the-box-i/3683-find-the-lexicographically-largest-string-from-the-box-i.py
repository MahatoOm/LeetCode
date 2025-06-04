class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends == 1:
            return word

        
        ans = ''
        diff = len(word) - numFriends + 1
        l = 0
        while l < len(word):
            
            ans  = max(ans , word[l : min(l+diff , len(word) )])


            l += 1

        return ans
