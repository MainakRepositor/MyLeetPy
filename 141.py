class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        l = code + code
        if k == 0:
            return [0]*n
        elif k > 0:
            ans = []
            for i in range(n):
                ans.append(sum(l[i+1:i+k+1]))
            return ans
        else:
            ans = []
            j = n
            for i in range(n):
                ans.append(sum(l[j+k:j]))
                j += 1
            return ans
        
