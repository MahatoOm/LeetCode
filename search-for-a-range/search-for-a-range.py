class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        result = []
        
        output = self.checkAvaibility(nums, target, True)
        if output != -1:
            result.append(output)
        else:
            return [-1, -1]

        rightmost = self.checkAvaibility(nums, target, False)
        if rightmost != -1:
            result.append(rightmost)

        return result

    def checkAvaibility(self, nums, target, status): 
        left ,right = 0 ,len(nums)-1

        while left  <= right:
            
            mid = (left + right )//2
            
            if nums[mid] == target:
                if  status == True:
                    if  mid  == 0 or nums[mid-1] < nums[mid]:
                        return mid
                    else:
                        right = mid - 1
                else:
                    
                    if mid + 1 == len(nums) or  nums[mid + 1] > nums[mid]:
                        return mid 
                    else:
                        left = mid + 1
                    
                
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
                
                
        return -1