class Solution:
    def maxDifference(self, s: str) -> int:
        
        ct = Counter(s)
        print(ct)
        odd_max = 0
        odd_min = inf
        even_max = 0
        even_min = inf
        for key, val in ct.items():
            if val % 2:
                
                odd_max = max(val, odd_max)
                odd_min = min(odd_min, val)
                
            else:
                even_max = max(even_max, val)
                even_min = min(even_min, val)

        return (odd_max - even_min)