class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        

        freq = Counter(nums)
        max_sets_allowded = len(nums) // k
        if max_sets_allowded == 1:
            return len(set(nums)) == len(nums)
        if max_sets_allowded <= 1:
            return False

        max_freq = max(freq.values())

        return max_freq <= max_sets_allowded
            
        