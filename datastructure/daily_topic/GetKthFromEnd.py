#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/2 6:24
# @File    : GetKthFromEnd.py


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        顺序遍历2次，第一次获得链表长度，第二次遍历到 n - k位置返回
        :param head:
        :param k:
        :return:
        """
        n = 0
        cur_node = head
        while cur_node:
            n += 1
            cur_node = cur_node.next

        ans_node = head
        for _ in range(n - k):
            ans_node = ans_node.next

        return ans_node

    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针，只需要遍历n
        :param head:
        :param k:
        :return:
        """
        fast = head
        for _ in range(k):
            fast = fast.next

        ans_node = head
        while fast:
            ans_node = ans_node.next
            fast = fast.next

        return ans_node
