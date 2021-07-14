#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/6 15:12
# @File    : RemoveNthFromEnd.py

"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        使用双指针，判断当前节点是否为倒数第n个节点
        :param head:
        :param n:
        :return:
        """

        pre_node = head
        node = head
        while node:
            # 判断是否是最后一个节点
            cur_node = node
            i = 0
            while cur_node and i < n:
                cur_node = cur_node.next
                i += 1

            if i == n and not cur_node:
                # 只有一个节点的情况
                if pre_node == node and n == 1:
                    return None
                # 删除头节点的情况
                elif pre_node == node:
                    return head.next
                # 当前节点为倒数第n个节点
                pre_node.next = node.next
                return head

            pre_node = node
            node = node.next

        return head

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        """
        使用dummy，快慢指针，让快指针先走n，然后和慢指针一起遍历，当快指针为None时，慢指针当前节点就是倒数第N个节点
        :param head:
        :param n:
        :return:
        """
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(0)
    cur_node = head
    for i in [1, 2]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    print(Solution().removeNthFromEnd(head.next, 2).val)
