class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        

        def isPrefixandSuffix(str1 , str2):
            n = len(str1)
            if n > len(str2):
                return False
            
            return str1 == str2[:n] and str1 == str2[-n:]
           
        
        count = 0
        for i in range(len(words)):

            for j in range(i+1, len(words)):
                # print(i , j)
                out = isPrefixandSuffix(words[i], words[j])

                if out is True:
                    count +=1

        return count
