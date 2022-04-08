#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (74.17%)
# Likes:    426
# Dislikes: 0
# Total Accepted:    226K
# Total Submissions: 304.8K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
# 
# 
# 示例 2:
# 
# 
# 输入： s = "God Ding"
# 输出："doG gniD"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 * 10^4
# s 包含可打印的 ASCII 字符。
# s 不包含任何开头或结尾空格。
# s 里 至少 有一个词。
# s 中的所有单词都用一个空格隔开。
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        return " ".join(s_list)
# @lc code=end

