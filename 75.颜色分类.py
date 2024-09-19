#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        right = 0
        left = len(nums) - 1
        i = 0
        while i <= left:
            if nums[i] == 0:
                self.swap(nums, right, i)
                right += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, i, left)
                left -= 1
        
        return nums
    
    def swap(self, nums, index1, index2):
        tmp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = tmp
# @lc code=end

