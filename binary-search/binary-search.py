class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def check( idx , n ):
            #Base condition to stop recursions
            if idx > n:
                return
            
            # mid contidion to get middle indedx
            mid = (idx + n) // 2

            # return mid if target is found
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                return check(mid+1 , n)
                
            else: 
                return check( idx, mid-1)

                
            # print(idx, n)
            
        

        return check (0, len(nums)-1) if target in nums else -1
        
