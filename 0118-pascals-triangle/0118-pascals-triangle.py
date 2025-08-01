class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for i in range(1, numRows):
            sec_result = []

            for j in  range(0 , (i // 2) + 1):

                if j == 0:
                    sec_result.append(1)
                    continue
                val  = result[i-1][j-1] +  result[i-1][j]
                sec_result.append(val)
            if i % 2 :
                rev = list(reversed(sec_result))
                result.append(sec_result + rev)
            else:
                rev = list(reversed(sec_result))
                result.append(sec_result + rev[1:] )
        return result