# class Solution:
#     def countGood(self, nums: List[int], k: int) -> int:
#         # nums_hash = { val : idx for idx, val in enumerate(nums)}
        

#         i =  0 
#         n = len(nums)

#         count_hash = defaultdict(int)
#         value_equal_to_k = 0
#         j = 0
#         result = 0
#         while i < n :
            
#             if nums[i] in count_hash:
#                 value_equal_to_k -= count_hash[nums[i]] * (count_hash[nums[i]] -1 )//2
#                 count_hash[nums[i]] += 1
#                 value_equal_to_k += count_hash[nums[i]] * (count_hash[nums[i]] -1 )//2

#             else:
#                 count_hash[nums[i]] = 1

#             if k <= value_equal_to_k :
#                 result += n-i
#                 while j <= i and k <= value_equal_to_k: 
#                     if count_hash[nums[j]] == 1:
#                         del count_hash[nums[j]]

#                     else:
#                         value_equal_to_k -= count_hash[nums[j]] * (count_hash[nums[j]] -1 )//2
#                         count_hash[nums[i]] -= 1
#                         value_equal_to_k += count_hash[nums[j]] * (count_hash[nums[j]] -1 )//2
#                     if k <= value_equal_to_k:
#                         result += n-i
#                     j+=1
#             i+=1
#         return result





from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        pairs = 0
        res = 0
        left = 0
        
        for right in range(len(nums)):
            val = nums[right]
            pairs += count[val]
            count[val] += 1

            # Shrink the window while we have enough pairs
            while pairs >= k:
                res += len(nums) - right
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1

        return res


            


