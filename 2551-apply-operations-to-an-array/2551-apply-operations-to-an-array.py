class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        answer = []
        for i in range(len(nums)-1):

            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            

        print(answer)
        for_zero = 0
        for_non_zero = 0
        count_of_zeroes = 0

        while for_zero < len(nums):


            # if nums[for_zero] == 0:
            #     while for_zero < len(nums) and nums[for_zero] == 0:
            #         for_zero += 1
            #     if for_zero < len(nums): 
            #         temp = nums[for_zero]
            #         nums[for_zero] = 0
            #         nums[for_non_zero] = temp

            if nums[for_zero] > 0:
                answer.append(nums[for_zero])
            else:
                count_of_zeroes += 1

            # for_non_zero +=1
            for_zero +=1
        print(answer)
        return answer + [0] * count_of_zeroes