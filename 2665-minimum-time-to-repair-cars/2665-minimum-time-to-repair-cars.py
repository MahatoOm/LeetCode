class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        low = 1
        high = max(ranks) * cars * cars # This is the maximum mum that can be achieved
        ans = high 

        # Appling Binary Search
        while low <=high:
            mid = low + (high-low) // 2

            if self.check_condition(ranks, cars, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def check_condition(self, ranks,cars, mid):
        
        cars_repaired = 0
        idx = 0

        while idx < len(ranks):

            val =  math.floor(math.sqrt(mid // ranks[idx]))

            cars_repaired += val

            if cars_repaired >= cars:
                return True
            idx += 1
        return False

