#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # 思路1: 暴力法，按顺序遍历每个字母的最大无重复子串
        # if len(s) == 0:
        #     return 0
        # maxlen = [1]
        # for i in range(len(s)):
        #     k = 1
        #     flag = True
        #     while flag and (i+k)<len(s) :
        #         if s[i+k] not in s[i:i+k]: 
        #             k = k+1
        #             maxlen.append(k)
        #         else:
        #             maxlen.append(k)
        #             flag = False
        # return max(maxlen)
    
        # 思路2: 滑动窗口法（减少重复判断） + 哈希集合（判断是否有重复字符）
        if not s: return 0
        occ = set()
        rk, ans = -1, 0
        n = len(s)
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while( rk+1 < n and s[rk+1] not in occ):
                occ.add(s[rk+1])
                rk = rk+1
            ans = max(ans, rk-i+1)
        return ans
            
# @lc code=end

