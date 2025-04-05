class Solution:
    
    def __init__(self):
        self.total_xor_sum = 0
    def subsetXORSum(self, nums: List[int]) -> int:
        
        visited = [False] * len(nums)
        self.make_sequence(nums, 0, visited,  0)

        return self.total_xor_sum

    
    def make_sequence(self, nums, j ,  visited, in_line_xor):

        # if len(possible_sequence) == 1:
        #     self.total_xor_sum += current_xor
        #     in_line_xor = current_xor
        # elif len(possible_sequence) > 1:
        self.total_xor_sum += in_line_xor
        for i in range(j,len(nums)):

            if not visited[i]:
                visited[i] = True
                self.make_sequence(nums, i, visited, in_line_xor ^ nums[i])
                visited[i] = False