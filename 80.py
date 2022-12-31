class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic={}
        letter=97
        for i in distance:
            dic[chr(letter)]=i
            letter+=1

        for i in set(s):
            first=s.index(i)
            last=s.rindex(i)
            diff=last-first-1
            if dic[i]!=diff:
                return False
        return True
