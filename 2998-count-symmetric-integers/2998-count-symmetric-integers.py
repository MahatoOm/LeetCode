class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        while low <= high:
            
            if len(str(low)) % 2 == 1:
                low += 1 
                continue
            else:
                strData = str(low)
                runTime = len(strData)/ 2
                i = 0
                sum_val = 0
                sum_second_val = 0
                for data in strData:
                    if i < runTime:
                        sum_val += int(data)
                        i += 1
                    else:
                        sum_second_val += int(data) 

                if sum_val == sum_second_val:
                    count +=1
                
            low += 1
        return count

