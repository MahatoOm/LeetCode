class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        pre_dict = {}
        for a , b in prerequisites:
            if b not in pre_dict:
                pre_dict[b] = deque()
            pre_dict[b].append(a)

        # print(pre_dict)

        def dfs(a, b):
            visited = set()
            stack = []
            stack.append(b)

            while stack:
                node = stack.pop()
                if a == node:
                    return True
                if node in visited or node not in pre_dict:
                    continue
                visited.add(node)
                next_node = pre_dict[node]
                for next_nodes in next_node:
                    if next_nodes not in visited:
                        stack.append(next_nodes)
            return False


        output = []
        for u, v in queries:
            
            output.append(dfs(u,v))
              
        return output