class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        zero_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            # If we have more than 1 zero in the window, shrink it from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate the length of the current window
            max_len = max(max_len, right - left + 1)
        
        return max_len


        # prev_sum = 0
        # max_val = 0
        # curr = False
        # dp = [0] * (len(nums)+1)
        # # print(len(nums))
        # current_no_of_ones = 0

        # for i  in range(len(nums)):
        #     element = nums[i]
        #     if element == 0: 
        #         # if curr:
        #         #     diff = dp[i] - prev_sum - 1
        #         #     dp[i+1] = diff + 1
        #         #     prev_sum = 0
        #         # else:
        #         #     dp[i+1] = dp[i] + 1 
        #         #     # prev_sum = 0                   
        #         #     curr = True
        #         max_val = max(max_val, current_no_of_ones)
        #         current_no_of_ones = 0



        #     else:
        #         # prev_sum += 1
        #         # dp[i+1] = dp[i] + 1
        #         current_no_of_ones += 1
            

        # return max(max_val, current_no_of_ones)

