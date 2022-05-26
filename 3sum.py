class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if (nums[i] == nums[i - 1] and i > 0):
                continue
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                threeSum = nums[i] + nums[l] + nums[r]
                
                if (threeSum < 0):
                    l += 1
                
                elif (threeSum > 0):
                    r -= 1
                    
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1
                        
        return result