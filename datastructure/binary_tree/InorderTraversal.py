#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 12:48
# @File    : InorderTraversal.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InorderTraversal(object):

    def __init__(self):
        pass

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        二叉树中序遍历，递归方式
        :param root:
        :return:
        """
        if not root:
            return []

        result = list()
        if root.left:
            result.extend(self.inorderTraversal(root.left))

        result.append(root.val)

        if root.right:
            result.extend(self.inorderTraversal(root.right))

        return result

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        二叉树中序遍历，递归方式，节约内存方式
        :param root:
        :return:
        """

        def inorder(root):
            if not root:
                return
            if root.left:
                inorder(root.left)

            result.append(root.val)

            if root.right:
                inorder(root.right)

        result = list()
        inorder(root)
        return result

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        二叉树中序遍历，迭代方式，使用栈
        :param root:
        :return:
        """
        stack = list()
        node = root
        result = list()
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result
