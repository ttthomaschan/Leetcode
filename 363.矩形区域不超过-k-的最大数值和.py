#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (49.10%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 63.8K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
# 
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# -10^5 
# 
# 
# 
# 
# 进阶：如果行数远大于列数，该如何设计解决方案？
# 
#

# @lc code=start
'''
解法一：滚动数组
遍历计算在不同边界情况下列和（或者行和），组合不同列和子数组可得到不同矩形区域的数值和。
'''
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):   # 枚举上边界
            total = [0] * n
            for j in range(i, m):   # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]   # 更新每列的元素和
                
                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)
        return ans

# @lc code=end

'''
解法二：动态规划
dp[i][j] -- 以（i，j）为右下角，（0，0）为左上角的矩形的数值和；
在记录更新dp[i][j] 的同时，遍历计算以（i，j）为右下角的所有矩形的数值和，并记录最大值max；
当max==k时，可以停止程序，返回最终值。
'''

if __name__ == "__main__":
    ''' SortedList 和 bisect_left 使用示例'''
    tmplist = SortedList([2,3,1,9,5])
    loc = tmplist.bisect_left(3)
    print(tmplist)
    print(loc)

    '''测试用例'''
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    sol = Solution()    
    ans = sol.maxSumSubmatrix(matrix,k)
    print(ans)