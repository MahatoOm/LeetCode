class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        l , r = 0 , 0
        count_of_operation = 0 
        while l < len(nums):

            while r < len(nums) and nums[r] == 1:
                r+=1

            l = r
            if l+2 < len(nums):
                nums[l] = 1
                count_of_operation += 1
            if l+1 < len(nums): 
                nums[l+1] ^= 1
                #flipping numbers using XOR operation
            if l+2 < len(nums):
                nums[l+2] ^= 1
            l+=1
            r+=1


        return count_of_operation if nums[-1] == 1 and nums[-2] == 1 else -1