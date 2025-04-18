class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
    # Second try using BFS
        def BFS(i):

            queue = deque()
            queue.append(i)
            while queue:
                node = queue.popleft()
                visited.add(node)

                for neighbor in Adjacent_graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)


        visited = set()
        Adjacent_graph = defaultdict(list)
        for i,j in edges:
            Adjacent_graph[i].append(j)
            Adjacent_graph[j].append(i)
        print(Adjacent_graph)

        result = 0
        for i in range(n):
            if i not in visited:
                result += 1
                BFS(i)

        return result

'''
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
'''