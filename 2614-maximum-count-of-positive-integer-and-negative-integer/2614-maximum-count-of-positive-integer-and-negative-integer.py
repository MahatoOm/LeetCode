class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # if 0 in nums:
        #     nums.remove(0)

        # print(nums)
        left = 0
        right =n = len(nums)
        if nums[left] > 0 or nums[-1] < 0:
            return n
        
        if nums[0] ==0 and nums[-1] == 0:
            return 0

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] == 0 :
                nums.remove(nums[mid])
                right -= 1
                n-=1
                continue

            if nums[mid] > 0:
                right = mid

            if nums[mid] < 0:
                left = mid


        return max(left+1, n - right)
        