class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        l = 1
        r = 0
        visited = defaultdict(bool)
        res = 0
        while r < len(nums):

            if visited[nums[r]]:
                while nums[l-1] != nums[r]:
                    visited[nums[l-1]] = False 
                    l += 1
                l += 1
            res = max(res, sum(nums[l-1:r+1]))
            visited[nums[r]] = True
            r += 1
        return res