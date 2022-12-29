class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dct = {"type": 0, "color": 1, "name": 2}
        key = dct[ruleKey]
        res = 0
        for item in items:
            if item[key] == ruleValue:
                res += 1
        return res
