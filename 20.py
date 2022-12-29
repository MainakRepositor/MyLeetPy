class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def getChars(word):
            for s in word:
                for c in s:
                    yield c
            yield
        
        return all(c1 == c2 for c1, c2 in zip(getChars(word1), getChars(word2)))
