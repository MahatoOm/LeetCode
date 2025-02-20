class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()

        n = len(nums)
        characters = ['0','1']
        possible_sequence = []

        # print(nums)

        self.generate_sequence(n, nums, characters, possible_sequence, 0 , '')
        # print(possible_sequence)
        i = 0
        for element in possible_sequence:
            
            if i< n and element == nums[i]:
                i+=1
            else:
                return element
        



    def generate_sequence(self, n, nums, characters, possible_sequence, i , current_char):
        if len(current_char) == n:
            
            possible_sequence.append(current_char)
            return

        
        for element in characters:

            self.generate_sequence(n, nums, characters, possible_sequence ,i, current_char + element)





