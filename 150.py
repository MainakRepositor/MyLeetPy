class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst=[]
        
        for i in range(0,rowIndex+1):
            
            temp=[]
            for j in range(0,i+1):
                
                # print('i {} j {}'.format(i,j))
                
                if  j==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(lst[i-1][j]+lst[i-1][j-1])
            lst.append(temp)
        
        return lst[rowIndex]
