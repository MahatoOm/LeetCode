class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #check if word from words1 is universal or not
        memo = []
        # words storage to store unique values from words2 and also those value which appears more than once
        words = []
        for w in words2:
            for char in w:
                if w.count(char) > 1:
                    words.append(char * w.count(char))
                else:
                    words.append(char)

        words = list(set(words)) 

        #function check to chect if all the words2 lies in word if yes add to storage memop
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
