class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))


'''

## Backtracking got TLE 47/49


class Solution:
    def __init__(self):
        self.ans = []

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        visited = [False] * len(nums)
        
        current_sequence = []
        self.backtracking( visited, nums ,current_sequence, 0 ,0)
        return self.ans


    def backtracking(self, visited, nums,current_sequence, curr_element , j):

        
        if len(self.ans)  < len(current_sequence):
            self.ans = current_sequence

        for i in range(j,len(nums)):
            if not visited[i] and (curr_element == 0 or nums[i] % curr_element ==0):
                visited[i] = True
                self.backtracking( visited, nums, current_sequence + [nums[i]], nums[i], i)
                visited[i] = False

'''



