class Solution:
    def relativeSortArray(self, A, B):
        k = {b: i for i, b in enumerate(B)}
        return sorted(A, key=lambda a: k.get(a, 1000 + a))
