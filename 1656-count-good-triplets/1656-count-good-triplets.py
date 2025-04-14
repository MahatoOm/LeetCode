class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        def enemuration(arr, i , a , b, c, n, visited, possible_sequence  ):
            nonlocal count
            if len(possible_sequence) == 3:
                if abs(possible_sequence[0] - possible_sequence[1]) <= a and abs(possible_sequence[1] - possible_sequence[2]) <= b and abs(possible_sequence[0] - possible_sequence[2]) <= c:
                    count += 1
                    return 
            if len(possible_sequence) > 3:
                return

            for curr in range(i ,n):
                if not visited[curr]:
                    visited[curr] = True
                    enemuration(arr, curr , a, b, c, n, visited, possible_sequence + [arr[curr]])
                    visited[curr] = False





        count = 0
        n = len(arr)
        visited = [False] * n 
        possible_sequence = []
        enemuration(arr, 0, a, b, c, n, visited, possible_sequence)

        return count