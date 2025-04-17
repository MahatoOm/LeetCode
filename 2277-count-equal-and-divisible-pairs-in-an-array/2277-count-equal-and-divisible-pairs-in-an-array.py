class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        left = 0
        count_map = defaultdict(list)
        result = 0
        for right in range(len(nums)):

            val  = nums[right]
            for idx in count_map[val]:
                if (idx * right) % k == 0:
                    result += 1

            count_map[val].append(right)
            


        return result


                

            






        