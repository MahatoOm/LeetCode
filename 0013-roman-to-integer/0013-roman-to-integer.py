class Solution:
    def romanToInt(self, s: str) -> int:

        roman_hash = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        l , r  = 0 , len(s)
        ans = 0
        while l < r:

            if l+1 < r and s[l] + s [l+1] in roman_hash:
                ans += roman_hash[s[l] + s[l+1]]
                l += 2
            else:
                ans += roman_hash[s[l]]
                l+=1

        return ans
            
        
