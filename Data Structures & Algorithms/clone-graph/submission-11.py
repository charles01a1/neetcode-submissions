"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return

        nodes_map = {}
        nodes_map[node] = Node(node.val, [])
    
        def dfs_clone(start_node, neighbour):
            if neighbour == None:
                return

            if neighbour not in nodes_map.keys() and start_node in nodes_map.keys():
                nodes_map[neighbour] = Node(neighbour.val, [nodes_map[start_node]])
                nodes_map[start_node].neighbors.append(nodes_map[neighbour])
                for i in neighbour.neighbors:
                    if i != start_node:
                        dfs_clone(neighbour, i)
            
            elif start_node in nodes_map.keys() and neighbour in nodes_map.keys():
                nodes_map[neighbour].neighbors.append(nodes_map[start_node])

        for child in node.neighbors:
            dfs_clone(node, child)

        return nodes_map[node]
