class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            row.sort()
        for j in range(len(grid[0])):
            maxVal = -float("inf")
            for row in grid:
                maxVal = max(maxVal, row[j])
            res += maxVal
        return res
