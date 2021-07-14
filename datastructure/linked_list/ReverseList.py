#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/6 15:58
# @File    : ReverseList.py
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/linked-list/f58sg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归算法
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        head_next = self.reverseList(head.next)
        head.next.next = head

        head.next = None
        return head_next

    def reverseList1(self, head: ListNode) -> ListNode:
        """
        迭代算法
        :param head:
        :return:
        """
        if not head:
            return None

        prev, cur = None, head
        while cur:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
        return prev


if __name__ == '__main__':
    head = ListNode(0)
    cur_node = head
    for i in [1, 2, 3, 4, 5]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    result = Solution().reverseList(head.next)
    for i in range(5):
        print(result.val)
        result = result.next
