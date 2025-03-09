from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0

        # Step 1: Create a helper array to check alternating pairs
        valid = [0] * n  # Stores 1 if colors[i] and colors[i+1] are different
        for i in range(n):
            if colors[i] != colors[(i + 1) % n]:
                valid[i] = 1

        # Step 2: Use a sliding window to check k-length valid segments
        curr_window_sum = sum(valid[:k-1])  # First k-1 alternating pairs
        for i in range(n):
            # Check if the full k-length window is alternating
            if curr_window_sum == k - 1:  
                count += 1
            
            # Slide window: Remove leftmost element and add new one
            curr_window_sum -= valid[i]  # Remove outgoing element
            curr_window_sum += valid[(i + k - 1) % n]  # Add incoming element

        return count


# class Solution:
#     def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
#         count = 0
        

#         # if diff_val

#         left = 0
#         right = len(colors)
#         while left < right:
#             diff_val = True

#             for i in range(left+1,k+left):

#                 if i < right:
#                     if colors[i-1] == colors[i]:
#                         diff_val = False
#                         left = i
#                         continue
#                 else:
#                     if colors[i-right-1] == colors[i-right]:
#                         diff_val = False
#                         left = i+right
#                         continue

#             if not diff_val:

#                 continue
#             count += 1
#             left+=1
#             while left  < right:
#                 if left + k < right:
#                     if colors[left+k-1] == colors[left+k]:
#                         left +=1
#                         continue

#                 else:
#                     if colors[left-right-1]== colors[left-right]:
#                         left+=1
#                         continue
#                 count +=1
#                 left +=1

#         return count


