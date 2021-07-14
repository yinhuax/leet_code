#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/27 16:44
# @File    : InorderTraversal.py
from typing import List

"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InorderTraversal(object):

    def __init__(self):
        pass

    def inorderTraversal(self, root: 'TreeNode') -> List[int]:
        result = []

        def dfs(node, result):
            if not node:
                return
            if node.left:
                dfs(node.left, result)

            result.append(node.val)

            if node.right:
                dfs(node.right, result)

        dfs(root, result)
        return result

    def inorderTraversal1(self, root: 'TreeNode') -> List[int]:
        # 遍历写法
        result = []
        stack = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)

            root = root.right

        return result


if __name__ == '__main__':
    pass
