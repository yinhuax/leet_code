#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/16 10:08
# @File    : MaxPathSum.py
"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        以当前节点为根节点，后续遍历计算最大路径和
        :param root:
        :return:
        """
        self.max_path = float('-inf')

        def postorder(node):
            if not node:
                return 0

            left_max = max(0, postorder(node.left))
            right_max = max(0, postorder(node.right))

            self.max_path = max(self.max_path, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        postorder(root)
        return self.max_path
