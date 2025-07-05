class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for key , val in Counter(arr).items():
            if key == val and val > res:
                res = val
        return res