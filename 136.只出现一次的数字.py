#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (72.07%)
# Likes:    2353
# Dislikes: 0
# Total Accepted:    650K
# Total Submissions: 901.6K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#
'''
方法一：
# 直接使用set()
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return  sum(nums_set)*2 - sum(nums)
'''

'''
方法二：
# 使用异或位运算
任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0 = a
任何数和其自身做异或运算，结果是 0，即 a⊕a = 0
异或运算满足交换律和结合律，即 a⊕b⊕a = b⊕a⊕a = b⊕(a⊕a) = b⊕0 = b
'''
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = nums[i] ^ sum
        return sum
# @lc code=end

