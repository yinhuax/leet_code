#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/6 18:06
# @File    : IsPalindrome.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        使用辅助栈，时间复杂度O（N），空间复杂度O(N)
        :param head:
        :return:
        """
        if not head:
            return True

        stack = []
        cur_node = head
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.next

        while head:
            last_node = stack.pop()
            if last_node.val != head.val:
                return False
            head = head.next

        return True

    def isPalindrome1(self, head: ListNode) -> bool:
        """
        使用快慢指针，边遍历，边翻转前面的链表，然后对比
        :param head:
        :return:
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        pre = head
        prev = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            pre.next = prev
            prev = pre

        if fast:
            slow = slow.next

        while pre and slow:
            if pre.val != slow.val:
                return False

            pre = pre.next
            slow = slow.next

        return True


if __name__ == '__main__':
    head = ListNode(0)
    cur_node = head
    for i in [1, 2, 1]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    result = Solution().isPalindrome(head.next)
    print(result)
