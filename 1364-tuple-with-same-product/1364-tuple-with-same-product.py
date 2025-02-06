from itertools import combinations
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        multiple_storage = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                multiple_storage[nums[i] * nums[j]].append((nums[i],nums[j]))
                
        # print(multiple_storage)
        count = 0
        for keyss in multiple_storage.keys():

            if len(multiple_storage[keyss]) >= 2:
                n = len(multiple_storage[keyss]) -1
                count += n * (n+1) // 2
        
        return 8 * count 







        # memory limit exceeded
        # all_numbers = list(combinations(nums, 4))
        # count = 0
        # for a,b,c,d in all_numbers:
        #     if a * b == c * d:
        #         count += 1
        #     if a * c == b * d:
        #         count += 1
        #     if a * d == b * c:
        #         count += 1

        # return 8 * count
