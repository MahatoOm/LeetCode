class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []
        i = 0
        extra = len(s) % k
        print(extra)
        while i + k <= len(s):

            res.append(s[i:i + k ])
            i += k

        rem = s[i:]
        print(rem +( fill * (k-extra)))
        if extra:
            res.append(rem +( fill * (k-extra)))
        return res