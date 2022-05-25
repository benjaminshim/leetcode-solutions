class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [0] * len(nums)
        elem = 0

        begin = 0
        end = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if (abs(nums[begin]) > abs(nums[end])):
                elem = nums[begin] ** 2
                begin += 1
                result[i] = elem
            else:
                elem = nums[end] ** 2
                end -= 1
                result[i] = elem
                
        return result