class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        
        prev = min(nums)
        res = 0
        for i in sorted(set(nums)):
            if i - prev == 1 :
                res = max(res, nums.count(i) + nums.count(prev))
            prev = i

        return res

