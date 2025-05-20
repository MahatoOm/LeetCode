class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        n = len(nums)
        check_list = [0] * (n + 1)
        for x, y in queries:

            check_list[x] += 1
            check_list[y + 1] -= 1

        print(check_list)
        val = 0
        for i in range(n):
            val += check_list[i]
            if val - nums[i] < 0:
                return False

        return True 
