class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        S = {*allowed}
        return sum(S.issuperset({*word}) for word in words)
