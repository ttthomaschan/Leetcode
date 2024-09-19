#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        maxN = 0
        sum_ = 0
        curValue = 0
        for i in range(n):
            sum_ = sum_ + customers[i]  * (1 - grumpy[i])
        
        for i in range(minutes):
            curValue = curValue + customers[i] * grumpy[i]
            maxN = max(curValue, maxN)
        
        for i in range(minutes, n):
            curValue = curValue - customers[i-minutes]*grumpy[i-minutes] + customers[i]*grumpy[i]
            maxN = max(curValue, maxN)
        
        return sum_+maxN
        
# @lc code=end

