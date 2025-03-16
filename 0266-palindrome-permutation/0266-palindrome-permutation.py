class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd_count = 0
        for char in set(s):
            if s.count(char) % 2 == 1:
                odd_count += 1

            if odd_count > 1:
                return False

        return True