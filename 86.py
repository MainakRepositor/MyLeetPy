class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l = len(arr)
        arr.sort()
        answer = [[arr[0], arr[1]]]
        difference = arr[1]-arr[0]
        for i in range(2, l):
            if arr[i] - arr[i-1]==difference: answer.append([arr[i-1], arr[i]])
            elif arr[i] - arr[i-1]<difference: 
                answer = [[arr[i-1], arr[i]]]
                difference = arr[i] - arr[i-1]
        return answer
