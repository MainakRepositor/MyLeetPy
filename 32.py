class Solution:
        def diagonalSum(self, mat: List[List[int]]) -> int:
            n = len(mat)
            return sum(row[r] + row[n - 1 - r] for r, row in enumerate(mat)) - (0, mat[n // 2][n // 2])[n % 2]
