class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)
        val = groups[0]
        curr =[words[0]]
        
        for i in range(1,n):

            if groups[i] != val:
                curr.append(words[i])
                val = groups[i]

        return curr

