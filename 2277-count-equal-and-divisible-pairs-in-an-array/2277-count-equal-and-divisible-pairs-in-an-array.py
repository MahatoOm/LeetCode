class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:        
        count_map = defaultdict(list)
        result = 0
        for right in range(len(nums)):           
            for idx in count_map[nums[right]]:
                if (idx * right) % k == 0:
                    result += 1
            count_map[nums[right]].append(right)
        return result


                

            






        