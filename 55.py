class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        
        # Search all rows
        for i in range(n):
            
            # Search all columns
            for j in range(m):
                
                # The current number is less than 0
                if grid[i][j] < 0:
                    res += 1
        
        return res
