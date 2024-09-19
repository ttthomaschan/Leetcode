#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            total = total - nums[i-k] + nums[i]
            maxSum = max(total, maxSum)
            
        return maxSum/k
# @lc code=end

