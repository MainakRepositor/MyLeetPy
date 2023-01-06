class Solution:
    def numRookCaptures(self, B: List[List[str]]) -> int:
        y, x = next((i, j) for j in range(8) for i in range(8) if B[i][j] == 'R')
        row = ''.join(B[y][j] for j in range(8) if B[y][j] != '.')
        col = ''.join(B[i][x] for i in range(8) if B[i][x] != '.')
        return sum('Rp' in s for s in (row, col)) + sum('pR' in s for s in (row, col))
