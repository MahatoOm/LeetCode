class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i , val in enumerate(nums):

            if target - val in nums[:i]:
                idx = nums.index(target-val)
                return [i, idx]


        