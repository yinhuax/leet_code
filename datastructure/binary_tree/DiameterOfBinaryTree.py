#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/16 15:41
# @File    : DiameterOfBinaryTree.py
"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_path = 0
        if not root:
            return self.max_path

        def dfs(node):
            """
            后续遍历，两个节点最大路径相加
            :param node:
            :return:
            """
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            self.max_path = max(self.max_path, left_path + right_path + 1)

            return max(left_path, right_path) + 1

        dfs(root)
        return self.max_path - 1
