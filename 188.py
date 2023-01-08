class Solution:
    #prefix sum
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums[1:])
        leftSum = 0
        #找pivot index
        for i in range(len(nums)-1):
            if leftSum == rightSum:
                return i
            #prefix sum
            leftSum += nums[i]
            rightSum -= nums[i+1] #有可能造成index out of range錯誤
        if rightSum == leftSum:
            return len(nums)-1
        return -1


