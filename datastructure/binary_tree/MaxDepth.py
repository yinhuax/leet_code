#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 13:36
# @File    : MaxDepth.py
from datastructure.binary_tree import TreeNode


class MaxDepth(object):

    def __init__(self):
        pass

    def maxDepth(self, root: TreeNode) -> int:
        """
        使用层次遍历方式
        :param root:
        :return:
        """
        from collections import deque
        queue = deque()
        queue.append(root)
        max_depth = 0

        if not root:
            return max_depth

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            max_depth += 1

        return max_depth

    def maxDepth1(self, root: TreeNode) -> int:
        """
        迭代方式，先序遍历，自顶向下
        :param root:
        :return:
        """

        def preorder(root, max_depth):
            if not root:
                return 0

            if not root.left and not root.right:
                self.result = max(self.result, max_depth + 1)

            if root.left:
                preorder(root.left, max_depth + 1)
            if root.right:
                preorder(root.right, max_depth + 1)

        self.result = 0
        preorder(root, 0)
        return self.result

    def maxDepth2(self, root: TreeNode) -> int:
        """
        迭代方式，先序遍历，自底向上
        :param root:
        :return:
        """
        if not root:
            return 0

        left_dep = self.maxDepth(root.left)
        right_dep = self.maxDepth(root.right)

        return max(left_dep, right_dep) + 1
