class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 2
        n = len(s)

        
        res = 0
        while right < n:
            data = s[left:right+1]
            while 'a' in data and 'b' in data and 'c' in data:
                res += n-right

                left +=1
                data = s[left:right+1]

            
            right += 1  

        return res