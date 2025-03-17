class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        count = Counter(nums)
        # print(count)
        
        for times in count.values():
            if times % 2 !=0:
                return False
                
        return True