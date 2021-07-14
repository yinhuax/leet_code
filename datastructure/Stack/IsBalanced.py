#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/25 8:01
# @File    : IsBalanced.py
"""
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
"""
from datastructure.binary_tree.Codec import Codec


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        深度优先遍历
        :param root:
        :return:
        """

        self.res = True

        def dfs(node, high):
            if not node:
                return high

            left_high = dfs(node.left, high) + 1
            right_high = dfs(node.right, high) + 1

            if abs(left_high - right_high) > 1:
                self.res = False

            return max(left_high, right_high)

        dfs(root, 0)
        return self.res


if __name__ == '__main__':
    code = Codec()
    # print(str([3, 9, 'null', 'null', 20, 15, 'null', 'null', 7, 'null', 'null']))
    root = code.deserialize(str([3, 9, 'null', 'null', 20, 15, 'null', 'null', 7, 'null', 'null']))
    print(Solution().isBalanced(root))
