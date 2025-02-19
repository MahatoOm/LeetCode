class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        num_stack = []

        # Iterate through the pattern
        for index in range(len(pattern) + 1):
            # Push the next number onto the stack
            num_stack.append(index + 1)

            # If 'I' is encountered or we reach the end, pop all stack elements
            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    result.append(str(num_stack.pop()))

        return "".join(result)


# class Solution:
#     def smallestNumber(self, pattern: str) -> str:
        
#         length = len(pattern)
#         possible_sequence = set()
#         seen = [False] * (length +1)
#         possible_string = [(i) for i in range(length+2)]
#         # print(possible_string)
#         # print(possible_sequence)

#         current_char = ""
#         self.generate_sequence(pattern, possible_sequence,possible_string , current_char , seen,"")
#         return current_char


#     def generate_sequence(self, pattern, possible_sequence,possible_string, current_char,  seen):

#         possible_string.append(current_char)
        
#         for pos,data in enumerate(possible_string):
#             if len(value) ==0 or len(current_char) ==0 and not seen[pos]: 
#             # if pos <len(pattern) and not seen[pos]:
#                 seen[pos] = True
#                 if cure
#                 current_char += str(data)
#                 self.generate_sequence(pattern, possible_sequence,possible_string, current_char ,  seen)
#                 seen[pos] = False
#                 current_char = current_char[:-1]



