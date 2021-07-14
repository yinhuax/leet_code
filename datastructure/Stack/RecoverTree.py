#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 22:49
# @File    : RecoverTree.py
"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 利用二叉搜索树，中序遍历为递增，找到错误的2个节点
        self.first_node = None
        self.second_node = None
        self.pre_Node = TreeNode(float('-inf'))

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if not self.first_node and self.pre_Node.val >= node.val:
                self.first_node = self.pre_Node
            if self.first_node and self.pre_Node.val >= node.val:
                self.second_node = node

            self.pre_Node = node
            dfs(node.right)

        dfs(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
