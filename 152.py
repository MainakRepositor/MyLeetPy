class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        a,n=[0]*101,len(logs)
        for birth,death in logs:
            a[birth-1950]+=1
            a[death-1950]-=1
        c=m=year=0
        for i in range(101):
            c+=a[i]
            if c>m:
                m=c
                year=i+1950
        return year
