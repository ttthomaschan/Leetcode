#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = count = 0
        for num in nums:
            if num == 1:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 0
        maxcount = max(maxcount, count)
        return maxcount
# @lc code=end

