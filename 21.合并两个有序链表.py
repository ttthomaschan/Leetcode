#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.69%)
# Likes:    2321
# Dislikes: 0
# Total Accepted:    950.3K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 
# l1 和 l2 均按 非递减顺序 排列
# 
# 
#
'''
方法一【递归】：
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.val =  self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.val =  self.mergeTwoLists(list1, list2.next)
            return list2 

                prehead = ListNode(-1)
'''
'''方法二【迭代】：'''
# @lc code=start
# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next
# @lc code=end

