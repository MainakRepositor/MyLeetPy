class Solution:
    def shortestToChar(self, S, C):
        n, pos = len(S), -float('inf')
        res = [n] * n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res
