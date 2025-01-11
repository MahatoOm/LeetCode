from collections import defaultdict
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        # creating hash table in ordert to store the count of character
        if len(s) < k:
            return False
        odd_count = 0
        char_dict = {}
        for char in set(s):
            char_count = s.count(char)
            if char_count %2 ==1:
                odd_count += 1
            char_dict[char] = char_count

        if odd_count > k:
            return False
        else:
            return True
