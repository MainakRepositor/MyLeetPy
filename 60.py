class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        unitOnTruck=0
        boxesOnTruck=0
        i=0
        while i<len(boxTypes) and boxesOnTruck<truckSize:
            k=min(boxTypes[i][0],truckSize-boxesOnTruck)
            boxesOnTruck+=k
            unitOnTruck+=boxTypes[i][1]*k
            i+=1
        return unitOnTruck
