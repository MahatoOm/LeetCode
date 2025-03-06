class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n= len(grid) #len of grid
        # value table hole 1 to n*n numbers to track repeated number and missing number
        val_table = [0] * (n*n)
        repeated_val = 0

        # accesing each element and updating the (index = element -1 )in value table
        for i in range(n):
            for j in range(n):
                element = grid[i][j]
                if val_table[element-1] != 0: # if there is already a value instead of 0 the element is repeated number
                    repeated_val = element

                val_table[element-1] = element


        # Now, there is only one index with value 0 THAT INDEX + 1 is our missing num
        missing_number = val_table.index(0) + 1
        # print(repeated_val)

        # print(val_table)

        # retuen in list format 
        return [repeated_val , missing_number]