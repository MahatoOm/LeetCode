class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp_max = [0] * (n+1)
        dp_min = [0] * (n+1)
        max_val = nums[0]
        min_val = nums[0]

        for i in range(n):
            data = nums[i]
            if dp_max[i] + nums[i] > 0:
                dp_max[i+1] = dp_max[i] + nums[i]
                max_val = max(max_val, dp_max[i+1],nums[i])

            if dp_min[i] + nums[i] < 0:
                dp_min[i+1] = dp_min[i] + nums[i]
            
            min_val = min(min_val, dp_min[i+1],nums[i])

        # print(max_val)
        # print(min_val)

        return max(abs(max_val), abs(min_val))
