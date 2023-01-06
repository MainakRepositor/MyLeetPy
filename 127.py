class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) != 1:
            new_nums = []
            j = 0
            for i in range(0, len(nums) - 1, 2):
                if j % 2 == 0:
                    new_nums.append(min([nums[i], nums[i + 1]]))
                else:
                    new_nums.append(max([nums[i], nums[i + 1]]))
                j += 1
            nums = new_nums
        return nums[0]
