#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/6 16:25
# @File    : RemoveElements.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        使用dummy节点+快慢指针
        :param head:
        :param val:
        :return:
        """
        if not head:
            return None

        dummy = ListNode(None, head)
        fast = head
        slow = dummy
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next

            fast = fast.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(0)
    cur_node = head
    for i in [1, 1]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    result = Solution().removeElements(head.next, 1)
    for i in range(4):
        print(result.val)
        result = result.next
