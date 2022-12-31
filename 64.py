class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return list(set(list(set(nums1) & set(nums2))+list(set(nums2) & set(nums3))+list(set(nums1) & set(nums3))))
