class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a=first
        for i in range(len(encoded)):
            encoded[i]=a ^ encoded[i]
            a=encoded[i]
        return [first]+encoded
