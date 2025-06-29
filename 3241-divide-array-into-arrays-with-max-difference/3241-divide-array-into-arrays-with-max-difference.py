class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(0, len(nums) , 3):
            if nums[i+2] - nums[i] <= k:
                output.append(nums[i: i+3])
            else:
                return [] 
        return output
