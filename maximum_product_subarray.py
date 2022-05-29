class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(nums)
        
        currMin, currMax = 1, 1
        
        for i in nums:
            if i == 0:
                currMin, currMax = 1, 1
            
            tmp = currMin
            currMin = min(currMin * i, currMax * i, i)
            currMax = max(tmp * i, currMax * i, i)
            result = max(currMax, result)
        return result