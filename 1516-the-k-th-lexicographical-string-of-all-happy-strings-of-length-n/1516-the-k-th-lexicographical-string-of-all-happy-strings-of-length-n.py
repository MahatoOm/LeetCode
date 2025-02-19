class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # all possible characters
        happy_strings = ["a","b","c"]
        #to store all possible strings
        possible_strings = []

        # seen = [False] * (len(happy_strings) + 1)

        #calling to generate possible strings of lenght n
        self.generate_strings(n,k, possible_strings, happy_strings, "")

        # print(possible_strings)

        if len(possible_strings) >= k:

            return possible_strings[k-1] 
        else:
            return ""

    def generate_strings(self, n , k , possible_strings, happy_strings, current_element):

        if len(current_element) == n:
            possible_strings.append(current_element)
            # we only need lennght of n no need to calculate further
            return
        
        for idx, element in enumerate(happy_strings):
            if len(current_element) == 0 or current_element[-1] != element:
                # seen[idx] = True
                self.generate_strings(n,k, possible_strings, happy_strings, current_element + element)
                # seen[idx] = False






