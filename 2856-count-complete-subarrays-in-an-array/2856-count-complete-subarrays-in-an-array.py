class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        total_distinct_element = len(set(nums))
        print(total_distinct_element)
        n = len(nums)
        i , j = 0, 0  
        result = 0
        while i <= n:

            if len(set(nums[j:i])) == total_distinct_element:
                result += (n-i+1)
                j += 1
                continue

            i += 1
        return result