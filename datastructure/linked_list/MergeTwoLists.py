#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/7 6:13
# @File    : MergeTwoLists.py

"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoLists(object):

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用遍历方式就行
        :param l1:
        :param l2:
        :return:
        """
        dummy_node = ListNode()
        pre_node = dummy_node

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
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

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        迭代方式
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    head = ListNode(0)
    cur_node = head
    for i in [1, 2, 3]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    head1 = ListNode(0)
    cur_node1 = head1
    for i in [1, 3, 4]:
        node = ListNode(i)
        cur_node1.next = node
        cur_node1 = node

    result = MergeTwoLists().mergeTwoLists(head.next, head1.next)
    for i in range(6):
        print(result.val)
        result = result.next
