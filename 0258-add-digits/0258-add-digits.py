class Solution:
    def addDigits(self, num: int) -> int:
        
        st = list(str(num))
        total = 0
        while True:
            for i in st:
                total += int(i) 
            # print(total)
            st = list(str(total)) 
            check = str(total)
            if len(check) == 1:
                return total
            total = 0

        return 0
