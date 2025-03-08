class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        n = len(blocks)
        # slided_window = 
        count_of_black = blocks[:k].count('W')
        # print(count_of_black)
        res = count_of_black

        for i in range(n-k):
            if blocks[i] == 'W':
                count_of_black -=1
            if blocks[i+k] == 'W':
                count_of_black +=1 

            res = min(res, count_of_black)


        return res 

