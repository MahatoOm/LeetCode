class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left , right = 0 , n-1

        while left <= right:

            mid = left + (right- left) // 2

            if nums[mid] > nums[n-1]:
                left  = mid +1
            else:
                right = mid -1

        

        def isBinarySearch( left , right):
            while left <= right:

                mid = left + (right - left) // 2

                if nums[mid] == target:
                    return mid
                if  nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return -1


        #pivot index = left index
        pivot = left

        # now check in two sorted array

        
        #wearching in first list
        output = isBinarySearch( 0 , pivot-1)
        if output != -1 :
            return output
        output = isBinarySearch(  pivot , n-1)
        if output != -1 :
            return output
        else:
            return -1

