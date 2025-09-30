class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n-1):
            new_num = []
            for j in range(n-i-1):

                if nums[j] + nums[j+1] >= 10:
                    new_num.append(nums[j] + nums[j+1] - 10)
                else:
                    new_num.append(nums[j] + nums[j+1])

            nums = new_num

        return nums[0]
