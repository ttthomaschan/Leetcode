#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        j = 0
        
        for i in range(0,N):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            
        for k in range(j,N):
            nums[k] = 0
            
        return nums
# @lc code=end

