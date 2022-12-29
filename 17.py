class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        #   [[9,9,8,1],
           # [5,6,2,6],
           # [8,2,6,4],
           # [6,2,2,2]]
            
        m=len(grid)
        n=len(grid)
        def findMax(x,y):
            print(x,y)
            maxi=-1
            for i in range(3):
                # print(grid[x+i][y:3])
                maxi=max(maxi,max(grid[x+i][y:3+y]))
            return maxi
        #m=4 n=4
        ans=[[0 for j in range(n-2)] for i in range(m-2)]
        # print(ans)
        for i in range(m-2):
            for j in range(n-2):
                ans[i][j]=findMax(i,j)
        return ans
                
            
                         
                    
                    
