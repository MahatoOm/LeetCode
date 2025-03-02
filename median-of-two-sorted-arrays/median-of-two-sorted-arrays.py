#
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na, nb = len(A), len(B)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            # If the segment of on array is empty, it means we have passed all
            # its element, just return the corresponding element in the other array.
            if a_start > a_end:
                return B[k - a_start]
            if b_start > b_end:
                return A[k - b_start]

            # Get the middle indexes and middle values of A and B.
            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = A[a_index], B[b_index]

            # If k is in the right half of A + B, remove the smaller left half.
            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            # Otherwise, remove the larger right half.
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)

        if n % 2:
            return solve(n // 2, 0, na - 1, 0, nb - 1)
        else:
            return (
                solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
                + solve(n // 2, 0, na - 1, 0, nb - 1)
            ) / 2



#  class Solution:
#     def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        
#         left_num1 = 0
#         right_num1 = len(num1)
#         left_num2 = 0
#         right_num2 = len(num2)
#         totalLen = len(num1) + len(num2)
#         total_move = totalLen // 2 

#         max_num = max(num1[-1],num2[-1])
#         min_num = min(num1[0],num2[0])
#         check = 0

#         while total_move:

#             if num1[left_num1] > num2[left_num2]:
#                 left_num2 +=1
#                 check = 2
#             else:
#                 left_num1 +=1
#                 check = 1
            
#             total_move -= 1

#         if totalLen % 2 == 1:
#             return num1[left_num1] if check == 1 else num2[left_num2]
#         else:
#             if check == 1:
#                 first_num = num1[left_num1-1] 
#                 second_num = num1[left_num1 + 1] if left_num1 < right_num1 and left_num2 < right_num2 and num1[left_num1] < num2[left_num2] else num2[left_num2 + 1]
#             else:
#                 first_num = num2[left_num2] 
#                 second_num = num2[left_num2 + 1] if num1[left_num1] > num2[left_num2] else num1[left_num1 + 1]
#             return (first_num + second_num) / 2

         
#         # return nums2[0]