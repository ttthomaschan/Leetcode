#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
# Note：
#   方法一： 前缀和 + 二分查找(Python bisect.bisect_left)
#   方法二： 滑动窗口
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
# @lc code=end

