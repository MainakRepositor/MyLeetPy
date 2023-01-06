class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        secs = 0 
        i = 0
        while tickets[k] != 0:
            if tickets[i] != 0: # if it is zero that means we dont have to count it anymore
                tickets[i] -= 1 # decrease the value by 1 everytime
                secs += 1 # increase secs by 1

            i = (i + 1) % len(tickets) # since after getting to the end of the array we have to return to the first value so we use the mod operator
            
        return secs
