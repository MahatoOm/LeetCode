import itertools
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        low = min(nums)
        high = max(nums)
        ans= 0

        while low <= high:

            mid = (low + high) // 2

            if self.check_condition(nums, k , mid):
                high = mid -1
                ans = mid
            else:
                low = mid + 1


        return ans

    def check_condition(self, nums, k ,mid):

        idx = 0
        house_robbed = 0
        while idx < len(nums):

            if nums[idx] <= mid:
                house_robbed += 1
                idx += 2
            else:
                idx += 1

        return house_robbed >= k 




        return True