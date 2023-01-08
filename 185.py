    def tictactoe(self, moves: List[List[int]]) -> str:
        row, col = [[0] * 3 for _ in range(2)], [[0] * 3 for _ in range(2)]
        d1, d2, id = [0] * 2, [0] * 2, 0
        for r, c in moves:
            row[id][r] += 1
            col[id][c] += 1
            d1[id] += r == c
            d2[id] += r + c == 2
            if 3 in (row[id][r], col[id][c], d1[id], d2[id]):
                return 'AB'[id]
            id ^= 1
        return 'Draw' if len(moves) == 9 else 'Pending'
