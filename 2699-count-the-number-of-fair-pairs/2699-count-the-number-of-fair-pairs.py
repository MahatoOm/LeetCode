class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.find_fair_pair_index(nums, upper+ 1) - self.find_fair_pair_index(nums, lower)


    def find_fair_pair_index(self,nums, element):
        left = 0
        right = len(nums)-1
        # upper_bound = upper - nums[0]
        # lower_bound = lower - nums[0]

        # print(upper_bound)
        # print(lower_bound)
        result = 0
        
        
        while  left < right  :
            val = nums[left] + nums[right] 
            if val  < element:
                result += right - left
                left += 1
            else:
                right -= 1


        return result 