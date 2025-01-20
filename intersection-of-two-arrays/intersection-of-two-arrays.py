class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums2.sort()
        
        
        def binary_lookup(nums, target):

            left = 0
            right = len(nums) -1
            while left <= right:
                mid = (left + right) //2

                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1

            return False
            



        result = []
        for data in set(nums1):
            if binary_lookup(nums2, data):
                result.append(data)

        return result