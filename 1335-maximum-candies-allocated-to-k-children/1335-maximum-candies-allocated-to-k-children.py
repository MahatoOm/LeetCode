class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies) < k :
            return 0


        low , high = 1 , max(candies)
        while low <= high:
            mid = (low + high ) // 2
            if self.check_conditions(candies , k , mid):
                ans = mid
                low = mid + 1
            else:
                high = mid -1

        return ans

    def check_conditions(self, candies, k , mid):
        duplicate_candies = 0

        for candy in candies:
            reminder = candy % mid
            quot = candy // mid

            # duplicate_candies.append(reminder)
            duplicate_candies += quot

        return duplicate_candies >= k         