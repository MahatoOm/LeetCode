class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        hash_map = {}
        total_pairs = (n* (n -1)//2)
        good_pairs = 0 
        #hash_map do it under o(n)
        for i in range(len(nums)):

            if nums[i]-i in hash_map:
                good_pairs += hash_map[nums[i]-i] 
                hash_map[nums[i]-i] +=1
            else:
                hash_map[nums[i]-i] = 1

        # print(hash_map)
        # print(good_pairs)
        # print(total_pairs)

        # brute force takes o(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i < j and j - i != nums[j] - nums[i]:
        #             count += 1

        return total_pairs-good_pairs