class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        

        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # skip the next index since both are used
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

        
        
        # nums.sort()

        # res = 0
        # i = 0
        # ans = []
        # for i in range(len(nums)-1):
           
        #     heapq.heappush(ans, [nums[i+1] - nums[i], i+1 , i])
        
        # visited = set()
        # unused = []
        # while ans:
        #     diff, x, y = heapq.heappop(ans)

        #     if x not in visited and y not in visited:
        #         visited.add(x)
        #         visited.add(y)
        #         p -= 1
        #     elif x not in visited:
        #         heapq.heappush(unused ,x)
        #     else:
        #         heapq.heappush(unused, y)

        #     while len(unused) >= 2:
        #         a = heapq.heappop(unused)
        #         b = heapq.heappop(unused)
        #         heapq.heappush(ans , [nums[b]-nums[a], b, a])

        #     if p == 0:
        #         break



        # return diff

        # for i in (sorted(ans.keys())):
        #     store = ans[i]

        #     res = max(res , i   )
        #     if p <= 0:
        #         break
        # print(ans)
        # return res

        # while i < p - len(nums)  and i < len(nums)-1:
        #     res = max(res, nums[i+1] - nums[i])
        #     i+=1

        # return res
