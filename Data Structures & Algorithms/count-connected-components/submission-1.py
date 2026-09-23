class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_graph = {i:[] for i in range(n)}

        for node,neigh in edges:
            adj_graph[node].append(neigh)        
            adj_graph[neigh].append(node)

        results = []
        visited = [False for i in range(n)]
        
        def dfs(node,par):
            if visited[node] == True:
                return False

            visited[node] = True
            for neigh in adj_graph[node]:
                if neigh != par:
                    dfs(neigh,node)
        

        result = 0

        for i in range(n):
            if visited[i] == False:
                result += 1
                dfs(i,-1)

        return result