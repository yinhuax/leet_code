#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/6 17:39
# @File    : OddEvenList.py
"""
奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/linked-list/fe0kj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        使用闪电双连鞭法，先分离奇数链，再分离偶数链，然后让奇数链尾部连接到偶数链头节点上
        :param head:
        :return:
        """
        if not head:
            return head

        even_head = head.next
        even = head.next
        odd = head
        while even and even.next:
            # 先让odd的next指向下一个odd
            odd.next = even.next
            odd = odd.next
            # 然后让even的next指向下一个even
            even.next = odd.next
            even = even.next

        # 最后让odd next 指向 even_head
        odd.next = even_head

        return head
