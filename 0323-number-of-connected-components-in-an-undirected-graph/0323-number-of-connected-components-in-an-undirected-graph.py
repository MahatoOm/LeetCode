class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # First try with DFS,
        def DFS(i):

            visited.add(i)
            for neighbor in Adjacent_graph[i]:
                if neighbor not in visited:
                    DFS(neighbor)

        visited = set()
        Adjacent_graph = defaultdict(list)
        for i,j in edges:
            Adjacent_graph[i].append(j)
            Adjacent_graph[j].append(i)
        
        result = 0
        for idx in range(n):

            if idx not in visited:
                result += 1
                DFS(idx)

        return result
