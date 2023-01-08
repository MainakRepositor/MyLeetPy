class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2=Counter(nums1),Counter(nums2)
        ans=[]
        for i in n1.keys() and n2.keys():
            ans.extend([i]*min(n1[i],n2[i]))
        return ans
