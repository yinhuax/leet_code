#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 14:51
# @File    : SortList.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        """
        归并排序实现，时间复杂度O（logn）, 空间复杂度 O(1)

        # 解题思路：  使用快慢指针，定位链表中间位置，拆分为左右两个链表
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid, slow.next = slow.next, None

        left, right = self.sortList(head), self.sortList(mid)

        # 合并左右两个链表
        h = res = ListNode(0)
        while left and right:
            if left.val <= right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next

            h = h.next

        h.next = left if left else right
        return res.next

    def sortList1(self, head: ListNode) -> ListNode:
        """
        快速排序
        :param head:
        :return:
        """
        new_head, _ = self.quick_sort(head)
        return new_head

    def quick_sort(self, head: ListNode) -> ListNode:
        if not head:
            return None, None

        # 使用head划分partition
        head1, p, head2 = self.partition(head)

        head1, end1 = self.quick_sort(head1)
        head2, end2 = self.quick_sort(head2)

        if end1:
            end1.next = p

        if p:
            p.next = head2

        new_head = head1 if head1 else p
        new_end = end2 if end2 else p
        return new_head, new_end

    def partition(self, head: ListNode) -> ListNode:
        if not head:
            return (None, None, None)

        head1, head2, = None, None
        node = head.next
        while node:
            new_node = node.next
            if node.val < head.val:
                if head1:
                    node.next = head1.next
                    head1.next = node
                else:
                    head1 = node
                    head1.next = None
            else:
                if head2:
                    node.next = head2.next
                    head2.next = node
                else:
                    head2 = node
                    head2.next = None

            node = new_node

        head.next = None
        return head1, head, head2
