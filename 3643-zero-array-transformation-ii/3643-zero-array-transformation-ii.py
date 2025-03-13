
class Solution:
    def is_zero_possible(self, nums, queries , k): 
        n = len(nums)
        DiffArr = [0] * (n+1) # Difference array to store as prefix sum

        for idx in range(k):
            l , r, val = queries[idx]

            # updating first left and right+1 with val
            DiffArr[l] += val
            if r + 1 < n:
                DiffArr[r + 1] -= val
        sum_value = 0
        for i in range(n):
            sum_value += DiffArr[i]
            if sum_value < nums[i]: 
                return False
        return True  # zero is formed

        # return all(DiffArr[i+1] < nums[i] for i in range(n)) 


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(queries)
        ans = n+1
        #tracking low and high possibilities
        left , right = 0 , n
    

        while left <= right:

            mid = (left + right )//2

            if self.is_zero_possible(nums , queries, mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

            
        return -1 if ans > n else ans