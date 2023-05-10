class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL:
                return 0
            if grid[row][col] == 1 or (row, col) in visited:
                return 1
            visited.add((row, col))

            return min(dfs(row -1, col), 
                dfs(row + 1, col), 
                dfs(row, col - 1), 
                dfs(row, col + 1))
 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0 and (r, c) not in visited:
                    res += dfs(r, c)
        
        return res
