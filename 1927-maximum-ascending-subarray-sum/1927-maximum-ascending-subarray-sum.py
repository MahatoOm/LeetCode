class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        output = max(nums)
        val = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):

            if nums[i] < nums[i+1]:
                val += nums[i] 
            else:
                
                output = max(output, val + nums[i])
                val = 0
        return max(output, val + nums[i+1])
