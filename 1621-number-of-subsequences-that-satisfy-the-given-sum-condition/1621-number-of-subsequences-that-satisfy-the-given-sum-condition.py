class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        cnt = 0
        MOD = 10 ** 9 + 7
        nums.sort()
        for i in range(len(nums)):
            min_val = nums[i]
       
            right = len(nums)-1
            left = i
            ans = left
            while left <= right:
                mid = (left + right)//2

                if nums[mid] + min_val <= target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1

                
            
            if ans > i:
                cnt += 2 ** (ans-i)
            elif 2 * min_val <= target:
                cnt += 1


        return cnt % MOD