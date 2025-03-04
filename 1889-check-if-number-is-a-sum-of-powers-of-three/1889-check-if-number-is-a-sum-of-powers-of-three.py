class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        while n > 0:

            if n % 3 == 2:
                return False

            n //= 3
        return True






    # Time Limit exceeded
    #     arr = []
    #     val = 0
    #     i = 0
    #     while val < n:

    #         val =  3**i
            
    #         if val == n:
    #             return True
    #         if val > n:
    #             break
    #         arr.append(val)
    #         i+=1
        
    #     seen = [False] * (len(arr)+1)
        
    #     sum_val = 0
        
    #     return self.generate_sequence(sum_val, seen, n, arr)
        
   

    # def generate_sequence(self, sum_val  , seen, target, arr):

        
    #     if sum_val == target:
    #         return True

    #     for idx, element in enumerate(arr):
    #         if not seen[idx]:
    #             seen[idx] = True
    #             if self.generate_sequence( sum_val + element, seen, target, arr):
    #                 return True
    #             seen[idx] = False

    #     return False