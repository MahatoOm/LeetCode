class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        l = 0
        times = 0
        el = max(nums)
        res = 0 
        n = len(nums)
        for r in range(len(nums)):
            if nums[r] == el:
                times += 1
            

            while l <= r and times >= k:
                res += (len(nums) - r   )
                if nums[l] == el:
                    times -= 1
                l += 1

        return res





