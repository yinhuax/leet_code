#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 16:52
# @File    : Connect.py


class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Connect(object):

    def __init__(self):
        pass

    def connect(self, root: 'Node') -> 'Node':
        """
        层序遍历方式
        :param root:
        :return:
        """
        # 空间复杂度O（N）使用队列
        if not root:
            return root

        from collections import deque
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                cur_node = queue.popleft()

                if i < size - 1:
                    cur_node.next = queue[0]

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return root

    def connect1(self, root: 'Node') -> 'Node':
        """
        使用额外空间O(1)
        :param root:
        :return:
        """
        if not root:
            return root

        pre = root
        while pre.left:
            tem = pre
            while tem:
                tem.left.next = tem.right
                if tem.next:
                    tem.right.next = tem.next.left

                # 继续向右遍历
                tem = tem.next

            # 从下一层的最左边开始遍历
            pre = pre.left

        return root

    def connect2(self, root: 'Node') -> 'Node':
        """
        递归方式，拉拉链做法
        :param root:
        :return:
        """

        def dfs(root):
            if not root:
                return
            left = root.left
            right = root.right

            while left:
                left.next = right
                left = left.right
                right = right.left

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root
