class Solution(object):
    def mostVisited(self, n, rounds):
        #If last value is greater than start value output list of numbers from start value to end value inclusive
        lastVal = rounds[len(rounds)-1]
        startVal = rounds[0]
        if lastVal > startVal:
            return [i for i in range(startVal,lastVal+1)]
        #If last value is equal to start value output list containing only start value
        elif lastVal == startVal:
            return [startVal]
        #If last value is less than start value output list containing values from lowest to end THEN start to highest
        elif lastVal < startVal:
            res = [i for i in range(1,lastVal+1)]
            res += [i for i in range(startVal,n+1)]
            return res
        else:
            return -1
