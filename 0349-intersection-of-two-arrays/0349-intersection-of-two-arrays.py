class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        for data in set(nums1):
            if data in nums2:
                output.add(data)
                
        return list(output)