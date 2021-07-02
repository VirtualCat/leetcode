class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = {}
        for i, tik in nums.length:
            if tik == 0:
                t[i] = nums[i]
            else:
                t[i] = nums[i] + t[i-1]
        
        return t