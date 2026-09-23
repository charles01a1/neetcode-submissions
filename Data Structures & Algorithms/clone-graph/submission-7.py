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
    
        for child in node.neighbors:
            self.dfs_clone(nodes_map, node, child)

        return nodes_map[node]

    def dfs_clone(self,nodes_map, start_node, neighbour):
        if neighbour == None:
            return

        if neighbour not in nodes_map.keys() and start_node in nodes_map.keys():
            nodes_map[neighbour] = Node(neighbour.val, [nodes_map[start_node]])
            nodes_map[start_node].neighbors.append(nodes_map[neighbour])
            for i in neighbour.neighbors:
                if i != start_node:
                    self.dfs_clone(nodes_map, neighbour, i)
        
        elif start_node in nodes_map.keys() and neighbour in nodes_map.keys():
            # nodes_map[start_node].neighbors.append(nodes_map[neighbour])
            nodes_map[neighbour].neighbors.append(nodes_map[start_node])

        # else:
        #     ## neighbour and start not in 
        #     nodes_map[node] = Node(start_node.val,[neighbour])
