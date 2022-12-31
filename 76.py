class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}
        
        for num in nums2:
            
            while(stack and num > stack[-1]):
                c = stack.pop()
                map[c] = num
            
            stack.append(num)
        
        return [map.get(e, -1) for e in nums1]
