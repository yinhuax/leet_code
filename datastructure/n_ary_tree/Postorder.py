#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 8:18
# @File    : Postorder.py
from typing import List

"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        迭代方式
        :param root:
        :return:
        """
        result = []

        def dfs(root):
            if not root:
                return

            for child in root.children:
                dfs(child)
            result.append(root.val)

        dfs(root)
        return result

    def postorder1(self, root: 'Node') -> List[int]:
        """
        递归方式
        :param root:
        :return:
        """
        if not root:
            return []

        # 使用栈
        stack = []
        stack.append(root)

        result = []
        while stack:
            cur_node = stack.pop()
            stack.extend(cur_node.children)
            result.append(cur_node.val)

        return result[::-1]
