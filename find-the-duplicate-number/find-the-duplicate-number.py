class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) 
        check = [0] * right
        while left < right:

            if check[nums[left]] != 0:
                return nums[left]
            check[nums[left]] = nums[left]
            
            left+=1



        # 'low' and 'high' represent the range of values of the target
        # low = 1
        # high = len(nums) - 1
        
        # while low <= high:
        #     cur = (low + high) // 2
        #     count = 0

        #     # Count how many numbers are less than or equal to 'cur'
        #     count = sum(num <= cur for num in nums)
        #     if count > cur:
        #         duplicate = cur
        #         high = cur - 1
        #     else:
        #         low = cur + 1
                
        # return duplicate
        
            
            