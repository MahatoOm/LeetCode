from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        result = []
        stack = []

        min_char = 'a'

        for ch in s:
            stack.append(ch)
            freq[ch] -= 1

            # Update min_char to the smallest character still available in s
            while min_char <= 'z' and freq[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from stack to result if top <= min_char
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        # Append remaining stack
        while stack:
            result.append(stack.pop())

        return ''.join(result)
