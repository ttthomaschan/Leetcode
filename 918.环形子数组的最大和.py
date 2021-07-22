#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums):
        def kadane(numList):
            if not numList:
                return float('-inf')
            ans = cur = numList[0]
            for x in numList[1:]:
                cur = x + max(cur,0)
                ans = max(ans, cur)
            return ans
        
        S = sum(nums)
        ans1 = kadane((nums))
        B = [-x for x in nums[1:]]
        ans2 = S + kadane(B)
        C = [-x for x in nums[0:len(nums)-1]]
        ans3 = S + kadane(C)
        
        return max(ans1, ans2, ans3)
# @lc code=end

if __name__ == "__main__":
    nums = [-2]
    sol = Solution()
    ans = sol.maxSubarraySumCircular(nums)
    print(ans)


'''
解题思路：
环形子数组最大和 --> 子数组最大和的进阶情况，会有 “单区间” 和 “双区间” 两种情况。
分类讨论 -
1）单区间：和普通子数组最大和相同
2）双区间：肯定是数组前段和后段取数，数组中段抛弃 --> 可以转化为 (Sum - 数组相反数的中段部分的最大值) [需注意保留头尾至少一个原素]
'''