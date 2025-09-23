class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        
        freq = Counter(nums)
        # print(freq)
        max_freq = max(freq.values())
        res = 0
        for x, y in freq.items():
            if y == max_freq :
                res += y
        return res