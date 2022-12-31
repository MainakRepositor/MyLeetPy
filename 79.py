class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        j=0
        for i in range(0,len(nums),2):
            nums[i]=a[j]
            nums[i+1]=b[j]
            j+=1
        return nums
