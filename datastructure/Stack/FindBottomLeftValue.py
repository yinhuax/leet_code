#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/25 8:27
# @File    : FindBottomLeftValue.py

"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1

"""

from datastructure.binary_tree.Codec import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        广度优先遍历
        :param root:
        :return:
        """
        from collections import deque
        queue = deque()
        queue.append(root)

        last_left = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    last_left = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return last_left

    def findBottomLeftValue1(self, root: TreeNode) -> int:
        """
        深度优先遍历
        :param root:
        :return:
        """
        res = [0, -1]

        def dfs(node, high):
            if node:
                if not node.left and not node.right and high > res[1]:
                    res[1] = high
                    res[0] = node.val

                dfs(node.left, high + 1)
                dfs(node.right, high + 1)

        dfs(root, 0)
        return res[0]


if __name__ == '__main__':
    code = Codec()
    # print(str([3, 9, 'null', 'null', 20, 15, 'null', 'null', 7, 'null', 'null']))
    root = code.deserialize(str([3, 9, 'null', 'null', 20, 15, 'null', 'null', 7, 'null', 'null']))
    print(Solution().findBottomLeftValue1(root))
