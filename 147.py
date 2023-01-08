class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        dictRanks = {}
        dictSuits = {}
        
        for key in ranks:
            dictRanks[key] = dictRanks.get(key, 0) + 1

        for key in suits:
            dictSuits[key] = dictSuits.get(key, 0) + 1
            
        maxRanks = max(dictRanks.values())
        maxSuits = max(dictSuits.values())
        
        if maxSuits == 5:
            return "Flush"
        if maxRanks >= 3:
            return "Three of a Kind"
        if maxRanks >= 2:
            return "Pair" 
        return "High Card"    
