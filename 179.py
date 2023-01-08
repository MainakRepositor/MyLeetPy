class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate90(mat):
            return [list(x[::-1]) for x in zip(*mat)]
        
        if sum(sum(row) for row in mat) != sum(sum(row) for row in target):
            return False

        for _ in range(4):
            mat = rotate90(mat)
            if mat == target:
                return True
        return False
