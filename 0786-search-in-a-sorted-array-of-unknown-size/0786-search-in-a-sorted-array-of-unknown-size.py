# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        left  = 0
        right = 10000
        count =0
                
        while left +1 < right:
            mid  = (left + right ) //2
            if ArrayReader.get(reader ,right) == 2 ** 31 -1:
                      
                right = mid
            else:
                mid = right 
                left = mid
                right = right + right//2
                # if mid == right:
                #     count +=1
                # if count == 2:
                #     break

            print(left, right)
        left = 0
        right = right + 1
        while left <= right:
            mid  = (left + right ) //2
                

            # print(left, right)
                
            if ArrayReader.get(reader,mid) == target:
                return mid
            
            if ArrayReader.get(reader, mid) >  target:
                right = mid - 1 
            if ArrayReader.get(reader, mid) < target:
                left = mid +  1  
        return -1