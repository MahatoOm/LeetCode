class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        idx = number.rfind(digit)
        max_return = "0"
        for i in range(len(number)):
            if number[i] == digit:
                data = number[:i] + number[i+1:]
                max_return = max(max_return, data)

        return max_return