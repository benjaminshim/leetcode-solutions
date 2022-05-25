class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        complements = {}
        complement = 0

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if (complement in complements):
                return [complements[complement], i]
            
            else:
                complements[nums[i]] = i
                