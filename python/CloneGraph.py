"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()

        def dfs(node: Optional['Node'], visited: dict) -> Optional['Node']:
            if not node: return None

            if node in visited:
                return visited[node]

            visited[node] = Node(node.val)

            for neighbor in node.neighbors:
                neighborCopy = dfs(neighbor, visited)
                visited[node].neighbors.append(neighborCopy)

            return visited[node]

        return dfs(node, visited)