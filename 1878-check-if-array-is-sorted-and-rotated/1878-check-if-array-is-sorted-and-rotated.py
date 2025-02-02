class Solution:
    def check(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums)

        # nums.sort()
        # for i in range(right-1):
        #     if nums[i] > nums[i+1]:
        #         return False
        # return True

        count = 0
        rotated = 0
        nonrotated = 0
        i = 0
        while i + 1 <  len(nums):

            if nums[i] > nums[i+1]:
                count += 1
            if count > 1:
                return False
            i += 1
        
        
        if count == 1:
            if nums[-1] <= nums[0]:
                return True
            else:
                return False
            
            
        return True
        
           

        
        


        # print(count)
        # print(i)


        # return count == rotated + nonrotated

            
        # while (left < right and nums[left] > nums[right] and nums[left] < nums[left+1]):

        #     left += 1

        # while left < right and nums[left] < nums[right] and nums[left] < nums[left+1]:

        #     left += 1

        # return left == right



        