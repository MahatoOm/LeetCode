from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        odd_count = 0
        even_count = 1  # Count of even prefix sums (prefix sum 0 is considered even)
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num
            
            # If current prefix sum is odd, it can form odd subarrays with even prefix sums
            if prefix_sum % 2 == 1:
                result += even_count
                odd_count += 1  # Count the current odd prefix sum
            else:
                result += odd_count
                even_count += 1  # Count the current even prefix sum
            
            result %= MOD  # Ensure result does not exceed 10^9 + 7

        return result


# class Solution:
#     def __init__(self):
#         self.count_of_odd_subarrays = 0
#         self.visited_sub_arrays = set()
#     def numOfSubarrays(self, arr: List[int]) -> int:
        
#         seen = [False] * len(arr)
#         visited_arr = ""

#         self.sumOfOddArrays(arr, visited_arr, 0, seen)
#         print(self.visited_sub_arrays)
#         return self.count_of_odd_subarrays

#     def sumOfOddArrays(self, arr, visited_arr, current, seen):
#         if visited_arr not in self.visited_sub_arrays and current % 2 == 1:
#             self.count_of_odd_subarrays +=1
#         self.visited_sub_arrays.add(visited_arr)


#         for i  in range(len(arr)):

#             if not seen[i]:
#                 seen[i] = True
#                 self.sumOfOddArrays(arr, visited_arr + str(arr[i]), current  + arr[i], seen)
#                 seen[i] = False
