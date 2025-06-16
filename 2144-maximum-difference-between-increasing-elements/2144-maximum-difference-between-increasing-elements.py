class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        res = -1
        # return max(res, max([nums[i+1] - nums[i] for i in range(len(nums)-1) if nums[i+1] > nums[i]]))
        for i in range(len(nums)-1):
            if max(nums[i+1:]) > nums[i]:
                res = max(res, max(nums[i+1:])- nums[i])

        return res
