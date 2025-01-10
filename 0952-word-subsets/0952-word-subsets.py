class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #check if word from words1 is universal or not
        memo = []
        
        words = []
        for w in words2:
            for char in w:
                if w.count(char) > 1:
                    words.append(char * w.count(char))
                else:
                    words.append(char)

        words = list(set(words)) 
        def check(word):
            for w in words:
                if len(w) <= word.count(w[0]):
                    continue
                else:
                    return

            memo.append(word)
            return

        for word in words1:
            check(word)


        return memo