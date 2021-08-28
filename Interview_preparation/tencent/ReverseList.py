#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/26 12:07
# @File    : ReverseList.py

# Definition for singly-linked list.

"""
反转链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        """
        翻转链表，迭代方式
        :param head:
        :return:
        """
        cur_node = head
        pre_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node

        return pre_node

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    pass
