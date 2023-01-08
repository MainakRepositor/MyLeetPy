"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index=abs(i)-1
            nums[index]=-1 * abs(nums[index])
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res
    
# EXPLANATION
    # First we will iterate through the array and change the element at indexes of present element to negative
    # (We will use abs because the value might be negative only once we have changed but we go to that element second time also
    # We will map element to their corresponding index here, like if we find 4, we will turn elelment at 3rd index to be negative. If we find 2, we will change element at 1st index to be negative. By doing so, we will change all the indexes corresponding to elements as negative and only absend element's index will be positive)
    # We will run another loop and if number in our array is positive, then we will add the element corresponding to its index in the result array
    #  ( for example, if element at index 2 is positive, we will add 3 in our result array)
