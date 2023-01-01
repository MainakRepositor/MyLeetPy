class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x=[]
        p=[]
       
        for i in range(0,numRows):
            for j in range(0,i+1):
                x.append(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)))
        
            p.append(x.copy())
            x.clear()
        return p
