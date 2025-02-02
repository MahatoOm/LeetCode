class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        '''
        intution - Binary Search + sliding window
        first sorting, so it it can be used for binary search iteration

        so the process is to find avg mid between high and low element and 
        count the total no of distances less than avg mid
        if no < k:
            adjust low to mid+1
        else:
            hight to mid
        return low



        '''    
        nums.sort()
    
        
        low = 0
        #max distance possible is high
        high = nums[-1] - nums[0]
        
        while low < high:
            
            mid = (low + high ) // 2
            count = self.count_low_distance_pairs(nums, mid)
            
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
    
    def count_low_distance_pairs(self, nums, max_distance):
        
        arr_size = len(nums)
        left = 0
        count = 0
        for right in range(arr_size):
            
            while nums[right] - nums[left] > max_distance:
                left +=1
            
            count += right - left
        return count
                
        
        