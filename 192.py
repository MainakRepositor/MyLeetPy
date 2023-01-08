class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        common = list(set1 & set2)
        d = {}
        for i in common:
            d[i] = list1.index(i) + list2.index(i)
        min_index= min(d.values())
        op = []
        for i in d:
            if d[i] == min_index:
                op.append(i)
        return op
