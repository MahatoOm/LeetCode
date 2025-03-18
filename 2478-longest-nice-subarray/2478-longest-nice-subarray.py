class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        count = 0
        # res = nums[0]
        right = len(nums) 
        
        # def count_nice_pairs(start , end = len(nums) -1):
        #     nonlocal max_count
        #     st = start
        #     if start + 1 > end:
        #         return max_count

        #     no = 1 
        #     while start + 1<= end and nums[start + 1] & nums[start] == 0:
        #         no +=1
        #         start += 1
        #     max_count = max(max_count, no)
        #     return count_nice_pairs( st, start )


        max_count = 1
        left = 0
        while left < right-max_count:
            
            used_bits = nums[left]
            count = 1

            for end in range(left+1, right):
            
                if used_bits & nums[end] == 0:
                    used_bits |= nums[end]

                    count += 1
                else:
                    break
            max_count = max(count, max_count)
            # print(max_count ,count, left)
            # if a:
            #     continue
            left+=1


        return max_count 

