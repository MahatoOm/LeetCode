from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            dist = {}
            step = 0
            while start != -1 and start not in dist:
                dist[start] = step
                start = edges[start]
                step += 1
            return dist

        # Get distances from both nodes
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        # Initialize answer
        min_node = -1
        min_distance = float('inf')

        for node in range(len(edges)):
            if node in dist1 and node in dist2:
                max_dist = max(dist1[node], dist2[node])
                if max_dist < min_distance or (max_dist == min_distance and node < min_node):
                    min_distance = max_dist
                    min_node = node

        return min_node


