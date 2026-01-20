from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i , val in enumerate(nums):

            j = 0
            while True:
                if j | j + 1 == val:
                    ans.append(j)
                    break
                elif j > val:
                    ans.append(-1)
                    break
                j+=1
            print(i , ans)
        return ans
    

if __name__ == "__main__":
    nums = [2,3,5,7]

    # ans = [-1 , 1, 4, 3]
    bo = Solution()
    res = bo.minBitwiseArray(nums)
    print(res)
