class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        result = derived[0]
        for i in range( 1 , n):

            result = result ^ derived[i] 


        return result == 0

