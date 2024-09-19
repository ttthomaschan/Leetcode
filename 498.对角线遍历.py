#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
# Note：
# 假设矩阵为n*m，则有
#   1. 对角线数量为 m+n+1
#   2. 第k条对角线，该对角线上所有点，横纵坐标之和为k(0 <= k <= m+n-1)
#   3. k为偶数（0，2，4...）时，横坐标x递减
#   4. k为奇数（1，3，5...）时，纵坐标y递减
#


# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        k = m + n - 1
        for i in range(k):
            if i % 2 == 0:
                x = i if i<m else m-1
                y = 0 if i<m else i-m+1
                while x >= 0 and y <= n-1:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
            else:
                y = i if i<n else n-1
                x = 0 if i<n else i-n+1
                while y >= 0 and x <= m-1:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            
        return ans
        
# @lc code=end
