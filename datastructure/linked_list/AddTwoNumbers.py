#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/7 6:31
# @File    : AddTwoNumbers.py
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/linked-list/fv6w7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        迭代求解，用额外O（1）存储每个位置剩下的
        :param l1:
        :param l2:
        :return:
        """
        dummy = ListNode()
        cur_node = dummy

        # 保留余下来的数
        carry = 0
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            sums = value1 + value2 + carry
            carry = sums // 10
            new_node = ListNode(sums % 10)
            cur_node.next = new_node
            cur_node = new_node

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用递归方式计算
        :param l1:
        :param l2:
        :return:
        """

        def dfs(l1, l2, carry, dummy):
            if not l1 and not l2 and not carry:
                return

            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            sums = value1 + value2 + carry

            carry = sums // 10
            new_node = ListNode(sums % 10)
            dummy.next = new_node
            dfs(l1.next if l1 else None, l2.next if l2 else None, carry, new_node)

        dummy = ListNode()
        dfs(l1, l2, 0, dummy)
        return dummy.next


if __name__ == '__main__':
    head = ListNode(0)
    cur_node = head
    for i in [9, 9, 9, 9]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    head1 = ListNode(0)
    cur_node1 = head1
    for i in [9, 9, 9, 9, 9, 9, 9]:
        node = ListNode(i)
        cur_node1.next = node
        cur_node1 = node

    result = Solution().addTwoNumbers1(head.next, head1.next)
    for i in range(8):
        print(result.val)
        result = result.next
