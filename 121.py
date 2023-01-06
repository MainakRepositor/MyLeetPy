class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        return sum(sorted(arr)[n // 20 : -n // 20]) / (n * 9 // 10)
