#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 13:51
# @File    : IsSymmetric.py
from datastructure.binary_tree import TreeNode

"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""


class IsSymmetric(object):

    def __init__(self):
        pass

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        迭代方式，使用层序遍历，使用两个队列，一个从左往右遍历，一个从右往左遍历，对比数值是否相同
        :param root:
        :return:
        """
        from collections import deque
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            left_node = queue.pop()
            right_node = queue.pop()
            if not left_node and not right_node:
                continue

            if (not left_node or not right_node) or left_node.val != right_node.val:
                return False

            queue.append(left_node.left)
            queue.append(right_node.right)
            queue.append(left_node.right)
            queue.append(right_node.left)

        return True

    def isSymmetric1(self, root: TreeNode) -> bool:
        """
        递归方式，对比镜像
        :param root:
        :return:
        """

        def recur(left, right):
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return recur(left.left, right.right) and recur(left.right, right.left)

        return recur(root.left, root.right) if root else True
