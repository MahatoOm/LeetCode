class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        res = 0
        similar = 0
        similar_used = 0
        
        word_hash = {}
        visited = set() 
        for word in (words):
            if word in visited :
                continue

            if word[0] == word[1] :

                if words.count(word) % 2 == 0 :
                    similar_used += (2* words.count(word) )
                else:

                    if similar  <= 2* words.count(word) :
                        
                        if similar:
                            similar_used += (similar - 2)    
                        similar =  (2* words.count(word) ) 
                    else:                        
                        similar_used += (2* (words.count(word) - 1) )


                
                
            elif word[1] + word[0] in words:

                res += (4 * (min(words.count(word), words.count(word[1] + word[0]))))
                visited.add(word[1] + word[0])
            visited.add(word)

         
        return  res + similar + similar_used
