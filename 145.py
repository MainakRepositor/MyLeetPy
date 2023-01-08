class Solution:
    def minimumCost(self, A):
        return sum(a for i,a in enumerate(sorted(A)) if (len(A) - i) % 3)
