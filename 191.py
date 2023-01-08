class Solution:
    def findLHS(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        # keep in dict the number of times each number appears:
        for num in nums:
            my_dict[num]+=1
            
        max_ = 0
        # for each number in dict check if it+its following number is more than previous max:
        for num in my_dict.keys():
            if my_dict.get(num+1):
                max_ = max(max_, my_dict[num] + my_dict.get(num+1))
        return max_
