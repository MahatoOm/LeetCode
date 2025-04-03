class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result , distance , high = 0,0,0
        for value in nums: 
            result = max(result, distance * value)
            distance = max(distance, high - value)
            high  = max(value, high)
        return result