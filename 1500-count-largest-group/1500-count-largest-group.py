class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        check_map = defaultdict(int)
        result = 0
        for i in range(1, n+1):
            sum_val = 0
            for char in str(i):
                sum_val += int(char)
            check_map[sum_val] += 1
            result = max(check_map[sum_val], result)
        # print(check_map)
        count = 0
        for item in check_map.values():
            if item == result:
                count += 1
        return count


