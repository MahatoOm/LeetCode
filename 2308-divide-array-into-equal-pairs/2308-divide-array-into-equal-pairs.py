class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        count = Counter(nums)
        # print(count)
        odd_count = 0
        for times in count.values():
            if times % 2 !=0:
                odd_count += 1

            if odd_count > 1:
                return False 
        return True