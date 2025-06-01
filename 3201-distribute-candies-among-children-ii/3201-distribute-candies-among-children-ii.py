class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:


        result = 0
        for i in range(min(n, limit)+1):

            left = max(0, n-i-limit)
            right = min(limit, n-i)
            result += ( max(min(limit, n - i) - max(0, n - i - limit) + 1, 0))

        return result
