#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/28 16:32
# @File    : MergeTwoLists.py

# Definition for singly-linked list.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = ListNode()

        cur_node = new_node
        while l1 and l2:
            if l1.val <= l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next

        while l1:
            cur_node.next = l1
            l1 = l1.next
            cur_node = cur_node.next

        while l2:
            cur_node.next = l2
            l2 = l2.next
            cur_node = cur_node.next

        return new_node.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        优化遍历
        :param l1:
        :param l2:
        :return:
        """
        dummy_node = ListNode()
        pre_node = dummy_node

        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    pre_node.next = l1
                    l1 = l1.next
                else:
                    pre_node.next = l2
                    l2 = l2.next
            elif l1:
                pre_node.next = l1
                l1 = l1.next
            else:
                pre_node.next = l2
                l2 = l2.next

            pre_node = pre_node.next

        return dummy_node.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        迭代写法
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2
