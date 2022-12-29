class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for c in accounts:
            max_wealth = max(max_wealth, sum(c))
        return max_wealth
