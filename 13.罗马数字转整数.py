#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        n = len(s)
        ans = 0
        for i, ch in enumerate(s):
            value = SYMBOL_VALUES[ch]
            if i < n-1 and value < SYMBOL_VALUES[s[i+1]]:
                ans -= value
            else:
                ans += value
        return ans
# @lc code=end

'''
## 思路总结：
通常情况下，罗马数字中小数字在大数字右边。
1）若满足上述情况，所有字符对应数值相加即可；
2）若一个数值右侧的数值比它大，则该数值符号取反即可。

'''
