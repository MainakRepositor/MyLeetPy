class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i_count = 0
        d_count = len(S)
        A = []
        for i in range(len(S)):
            if(S[i] == 'I'):
                A.append(i_count)
                i_count += 1
                
            else:
                A.append(d_count)
                d_count -=1
                
        A.append(i_count)
                
        return A
