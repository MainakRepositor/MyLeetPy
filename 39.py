class Solution(object):
    def oddCells(self, row_n, col_n, indices):
        grid = [0]*row_n*col_n
        for ri,ci in indices:
            row = ri*col_n
            grid[row:row+col_n] = [1+v for v in grid[row:row+col_n]]
            grid[ci::col_n] = [1+v for v in grid[ci::col_n]]

        odds = 0
        for n in grid:
            if n % 2:
                odds += 1

        return odds
