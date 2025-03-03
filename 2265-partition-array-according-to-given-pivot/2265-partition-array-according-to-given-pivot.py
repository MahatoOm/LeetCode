class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = []         
        high = []         
        count = 0         
        for element in nums:
            if element < pivot :
                low.append(element)
            elif element > pivot:
                high.append(element)
            else:
                count +=1


        return low + [pivot] * count + high







'''
nums = [9,12,5,10,14,3,10]
i = 0 , j = 0 element < pivot 
nums = [9,12,5,10,14,3,10]
i = 1 , j = 1   ,element > pivot 
nums = [9,12,5,10,14,3,10]
i = 1 , j = 2   ,element < pivot 
nums = [9,12,5,10,14,3,10]
swap  i and j ,
nums = [9,5, 12,10,14,3,10]
i = 2 , j = 2 element > pivot 
    j = 3 element = pivot 
    swap i , j
nums = [9,5,10, 12,14,3,10]
i = 3 , j =4 >
i = 3 , j = 5 < 







'''