class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2):

            for j in range(i+1,n-1):

                val = (nums[i] - nums[j]) * max(nums[j+1:])

                res = max(res , val)


        return res
