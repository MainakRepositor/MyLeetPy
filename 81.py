class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = set()
        
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
        
        for n in nums2:
            if n in hashmap:
                res.add(n)
                
        return res
