class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        dic = Counter(str(digits))
        l1 = [i for i in range(100,1000,2)]
        return list(filter(lambda x:Counter(str(x)) <= dic,l1))
