class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res=0
        m,n=len(strs),len(strs[0])
        strs=["".join ([strs[i][j] for i in range(m)]) for j in range (n)]
        for i in strs:
            if i!="".join(sorted(i)):
                res+=1
        return res
