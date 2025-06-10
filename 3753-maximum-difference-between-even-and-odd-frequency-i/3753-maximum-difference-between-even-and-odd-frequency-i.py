class Solution:
    def maxDifference(self, s: str) -> int:
        
        ct = Counter(s)
        odd_max = 0
        even_min = inf
        for key, val in ct.items():
            if val % 2:
                odd_max = max(val, odd_max)
            else:
                even_min = min(even_min, val)

        return (odd_max - even_min)