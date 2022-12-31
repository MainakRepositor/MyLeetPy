class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        temp = []
        ind = s.index(c)
        for i in range(len(s)):
            if abs(ind-i)>abs(s.find(c,i)-i):
                ind = s.index(c,i)
            if s[i]!=c:
                temp.append(abs(ind-i))
            else:
                temp.append(0)
        return temp
