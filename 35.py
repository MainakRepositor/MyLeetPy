class Solution(object):
    def minTimeToVisitAllPoints(self, p):
        return sum(max(abs(p[i-1][0] - p[i][0]), abs(p[i-1][1] - p[i][1])) for i in range(1, len(p)))
