class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = [[False for _ in range(len(grid[0]))]for _ in range(len(grid))]
        
        for r in range(len(grid)):
            for l in range(len(grid[0])):
                if grid[r][l] == "1" and visited[r][l] == False:
                    num_islands += self.dfs(grid,visited, r, l)

        return num_islands

    
    def dfs(self,grid,visited: List[List[bool]], start_row, start_col):
        if visited[start_row][start_col]:
            return 0   

        visited[start_row][start_col] = True
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        for direction in directions:
            r,l = direction[0],direction[1]
            if 0 <= start_row + r < len(visited) and 0 <= start_col + l < len(visited[0]):
                if grid[start_row + r][start_col + l] == "1": 
                    # visited[start_row + r][start_col + l ] = True
                    self.dfs(grid,visited, start_row + r, start_col + l )
                # visited[start_row + r][start_col + l ] = True

        return 1  
