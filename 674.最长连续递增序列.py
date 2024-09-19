#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        j = 0
        res = 0
        for i in range(1,N):
            if nums[i-1] < nums[i]:
                j += 1
                res = max(res, j)
            else:
                j = 0
        
        return res + 1
# @lc code=end

