class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_graph = {i:[] for i in range(n)}

        for node, neigh in edges:
            adj_graph[node].append(neigh)
            adj_graph[neigh].append(node)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for neigh in adj_graph[node]:
                adj_graph[neigh].remove(node)
                if not dfs(neigh): return False
            
            return True

        
        val = dfs(0)
        if val == False:
            return False
        
        if len(visited) == n:
            return True
        
        return False
