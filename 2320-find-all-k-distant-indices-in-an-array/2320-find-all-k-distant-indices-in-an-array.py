class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        if len(set(nums)) == 1 and nums[0] == key:
            return [i for i in range(len(nums))]

        i = 0
        res = []
        while i < len(nums):
            
            if nums[i] == key:
                
                j = i-k if i >= k else 0
                while j <= i + k and 0 <= j < len(nums) :

                    if j not in res:
                        res.append(j)
                    j += 1
            

            i += 1
        return res
            

                