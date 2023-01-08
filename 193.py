class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0 # taking counter for $5
        count10 = 0 # taking counter for $10
        for b in bills: # treversing the list of bills.
            if b == 5: 
                count5+=1 # if the bill is 5, incresing the 5 counter.
            elif b == 10:
                if count5 == 0: # if the bill is 10 & we dont have change to return, then its false.
                    return False
                count10+=1 # increasing the 10 counter
                count5-=1 # decreasing 5 counter as we`ll give 5 as change. 
            else: # if the bill is of $20
                if (count5>=1 and count10>=1):# checking if we have enough change to return
                    count5-=1 # if its a $20 , then $5 as change and 
                    count10-=1 # one $10
                elif count5>=3: # fi we dont have $10 as change, though we have three $3.
                    count5-=3 # decresing the $3 counter. 
                else:
                    return False
        return True
        
        ```
***Found helpful, Do upvote !!***
