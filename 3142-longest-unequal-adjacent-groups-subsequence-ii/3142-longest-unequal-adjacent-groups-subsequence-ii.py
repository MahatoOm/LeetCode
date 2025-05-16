class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (
                    self.check(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev_[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev_[i]
        ans.reverse()
        return ans

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

# class Solution:
#     def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:        
#         n= len(words)
#         ans = []
        
#         for i in range(n-1):
#             curr = [words[i]]
#             l = i
#             for j in range(i+1, n):

#                 if groups[l] == groups[j] or len(words[l]) != len(words[j]):
#                     continue

#                 diff = sum( x!=y for x, y in zip(words[l],words[j])) 
#                 if diff == 1:
#                     curr.append(words[j])
#                     l = j
                    

#             if len(curr) > len(ans):
#                 ans = curr


#         return ans
                

