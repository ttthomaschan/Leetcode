#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        n = len(nums)
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
            else:
                fast += 1
        return slow
# @lc code=end

