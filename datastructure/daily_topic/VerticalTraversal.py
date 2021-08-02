#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/31 13:57
# @File    : VerticalTraversal.py

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """
        层序遍历变形题，以根节点(0, 0) 开始，(i, j)，往下遍历时 左边节点为 (i + 1, j - 1)，右边节点为(i + 1, j + 1)

        使用字典存储每列对应的值，返回结果时转换数据
        :param root:
        :return:
        """
        nodes = list()

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return

            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()
        ans, lastcol = list(), float("-inf")

        for col, row, value in nodes:
            if col != lastcol:
                lastcol = col
                ans.append(list())
            ans[-1].append(value)

        return ans
