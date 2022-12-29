class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out = 0
        for o in operations:
            out += 1 if "+" in o else -1
        return out
