class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odds = sum(x % 2 for x in chips)
        return min(odds, len(chips) - odds)
