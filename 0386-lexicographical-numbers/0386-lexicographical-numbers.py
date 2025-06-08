class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def find_optimal_values(start):
            if start > n :
                return
            res.append(start)
            for i in range(10):
               find_optimal_values((start * 10) + i)


        res = []
        for i in range(1,10):
            find_optimal_values( i)
            


        return res