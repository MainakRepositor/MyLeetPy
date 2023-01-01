class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]])->bool:
        r_len, c_len = len(matrix),len(matrix[0])
        
        for r in range (1, r_len):
            for c in range (1, c_len):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        
        return True
