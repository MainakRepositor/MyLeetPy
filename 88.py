class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        freq1, freq2 = Counter(words1), Counter(words2)
        return len({w for w, v in freq1.items() if v == 1} & {w for w, v in freq2.items() if v == 1}) 
        
        
       
