#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N<2 :
            return N
        j,k = 1,1
        for i in range(1,N):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
                k = 1
            elif nums[i] == nums[i-1] and k<2:
                nums[j] = nums[i]
                j += 1
                k += 1
            else:
                k += 1
        return j
# @lc code=end

