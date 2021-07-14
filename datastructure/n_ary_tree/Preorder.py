#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 7:07
# @File    : Preorder.py
from typing import List

"""
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        前序遍历，递归方式
        :param root:
        :return:
        """
        result = []

        def dfs(root):
            if not root:
                return
            # 根左右
            result.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return result

    def preorder1(self, root: 'Node') -> List[int]:
        """
        迭代方式，
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
            result.append(cur_node.val)
            stack.extend(cur_node.children[::-1])

        return result
