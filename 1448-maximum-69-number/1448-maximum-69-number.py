class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ""
        n = str(num)
        i=1
        
        a = 1
        for i in n:
            if i == "6" and a :
                res += "9" 
                a = 0 
                continue

            res += i


        return int(res) 