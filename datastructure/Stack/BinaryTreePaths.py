#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/25 8:17
# @File    : BinaryTreePaths.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = set()

        def dfs(node, path):
            if node:
                path += str(node.val) + "->"
                if not node.left and not node.right:
                    result.add(path[:-2])
                    return

                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return list(result)
