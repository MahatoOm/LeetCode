class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        total = 0
        prev = 0
        for i , val in  enumerate(nums):

            if val == 0:
                prev += 1
            else:
                total += prev * (prev + 1) / 2
                prev = 0


        if prev:
            total += prev * (prev + 1) / 2
        return int(total)

