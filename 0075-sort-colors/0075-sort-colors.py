class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for idx in range(len(nums) -1):
            for s_idx in range(idx +1 , len(nums)):
                if nums[idx] > nums[s_idx]:
                    nums[idx] , nums[s_idx] = nums[s_idx] , nums[idx] 
        