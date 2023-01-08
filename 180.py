class Solution:
    def maxCount(self, m, n, ops):
        return min(i for i,_ in ops+[[m,n]]) * min(j for _,j in ops+[[m,n]])
