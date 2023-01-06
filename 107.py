class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, ct = 0, collections.Counter
        chars_counter = ct(chars)
        for word in words:
            word_counter = ct(word)
            if all(word_counter[c] <= chars_counter[c] for c in word_counter):
                sum += len(word)
        return sum
