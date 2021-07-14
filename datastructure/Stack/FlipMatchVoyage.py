#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 8:16
# @File    : FlipMatchVoyage.py
from typing import List

"""
给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。

另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 结果。

通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下：


请翻转 最少 的树中节点，使二叉树的 先序遍历 与预期的遍历行程 voyage 相匹配 。 

如果可以，则返回 翻转的 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 [-1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flip-binary-tree-to-match-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        翻转二叉树
        :param root:
        :param voyage:
        :return:
        """
        # 深度优先遍历，对比当前节点与voyage是否相同
        self.i = 0
        self.filp_list = []

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.filp_list = [-1]
                    return

                self.i += 1
                if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                    self.filp_list.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.filp_list and self.filp_list[0] == -1:
            self.filp_list = [-1]
        return self.filp_list
