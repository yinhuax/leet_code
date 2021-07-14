#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/6 8:26
# @File    : GetIntersectionNode.py
"""
LC 相交链表
编写一个程序，找到两个单链表相交的起始节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        只要知道两个链表的长度，就可以知道是否相交，L1 = len(headB) L2 = len(headA), L_max = max(L1, L2), 让长链表先遍历L_max - L_min次
        ，然后两个链表一起遍历，如果相交，必能走到同一节点
        :param headA:
        :param headB:
        :return:
        """
        l_a = 0
        node_a = headA
        while node_a:
            node_a = node_a.next
            l_a += 1

        l_b = 0
        node_b = headB
        while node_b:
            node_b = node_b.next
            l_b += 1

        if l_a > l_b:
            min_node = headB
            max_node = headA
            diff = l_a - l_b
        else:
            min_node = headA
            max_node = headB
            diff = l_b - l_a

        while diff > 0:
            max_node = max_node.next
            diff -= 1

        while min_node != max_node:
            min_node = min_node.next
            max_node = max_node.next

        return min_node


if __name__ == '__main__':
    head_A = ListNode(0)
    a_1 = ListNode(9)
    a_2 = ListNode(1)
    a_3 = ListNode(2)
    a_4 = ListNode(4)
    head_A.next = a_1
    a_1.next = a_2
    a_2.next = a_3
    a_3.next = a_4

    head_B = ListNode(3)
    head_B.next = a_3

    print(Solution().getIntersectionNode(head_A, head_B).val)
