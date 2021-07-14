#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 13:08
# @File    : PostorderTraversal.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PostorderTraversal(object):

    def __init__(self):
        pass

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后序遍历，递归写法
        :param root:
        :return:
        """

        def postorder(root):
            if not root:
                return

            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)

            result.append(root.val)

        result = []
        postorder(root)
        return result

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        后序遍历，迭代写法，使用栈
        :param root:
        :return:
        """
        stack = []
        pre = None
        node = root
        result = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if not node.right or node.right == pre:
                # 当前节点没有right或者right已经被遍历过，直接append值
                result.append(node.val)
                pre = node
                node = None
            else:
                # 此时根节点未遍历
                stack.append(node)
                node = node.right

        return result
