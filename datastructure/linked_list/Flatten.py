#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/7 7:04
# @File    : Flatten.py

"""
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。
这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/linked-list/fw8v5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def flatten(self, head: 'Node') -> 'Node':
        """
        递归方式
        :param head:
        :return:
        """

        def dfs(cur_node):
            if not cur_node:
                return

            child = cur_node.child
            next = cur_node.next
            self.prev_node.next = cur_node
            cur_node.prev = self.prev_node
            self.prev_node = cur_node

            dfs(child)
            cur_node.child = None
            dfs(next)

        dummy = Node(None, None, None, None)
        self.prev_node = dummy
        dfs(head)

        if head:
            head.prev = None
        return dummy.next

    def flatten1(self, head: 'Node') -> 'Node':
        """
        使用栈实现迭代方式
        :param head:
        :return:
        """
        if not head:
            return None

        dummy = Node(None, None, None, None)
        prev_node = dummy

        stack = head and [head]
        while stack:
            cur_node = stack.pop()

            # 修改新链表的指针节点
            prev_node.next = cur_node
            cur_node.prev = prev_node

            # 先把主线入栈
            if cur_node.next:
                stack.append(cur_node.next)

            # 然后支线入栈
            if cur_node.child:
                stack.append(cur_node.child)
                cur_node.child = None

            prev_node = cur_node

        dummy.next.prev = None
        return dummy.next
