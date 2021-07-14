#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/8 7:33
# @File    : RotateRight.py
"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        旋转链表
        :param head:
        :param k:
        :return:
        """
        if not head or not head.next:
            return head

        # 遍历链表获取链表长度，让链表最后一个节点指向头节点，形成环
        n = 1
        old_tail = head
        while old_tail.next:
            n += 1
            old_tail = old_tail.next

        old_tail.next = head
        # 遍历到第n - k%n - 1
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
