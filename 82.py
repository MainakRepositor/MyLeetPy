class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = [min(i) for i in matrix]
        maxs = [max(i) for i in zip(*matrix)]
        return list(set(maxs) & set(mins))
