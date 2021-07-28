#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/28 8:13
# @File    : DistanceK.py
from typing import List

"""
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        解题思路:
             1. 从target 深度遍历所有距离为k的节点
             2. 从左右节点以及父结点开始遍历
             3. 需要保存当前节点的父结点关系
        :param root:
        :param target:
        :param k:
        :return:
        """
        # 深搜保存每个节点值对应的父节点关系，使用map保存
        fathers = dict()

        def dfs_find_father(node):
            if not node:
                return

            if node.left:
                fathers[node.left.val] = node
                dfs_find_father(node.left)

            if node.right:
                fathers[node.right.val] = node
                dfs_find_father(node.right)

        dfs_find_father(root)

        ans = []

        # 深搜左右节点、父结点，找到距离target深度为k的所有节点
        def find_ans(node, pre_node, depth):
            if not node:
                return

            if depth == k:
                ans.append(node.val)
                return

            # 遍历左节点
            if node.left != pre_node:
                find_ans(node.left, node, depth + 1)

            # 遍历右节点
            if node.right != pre_node:
                find_ans(node.right, node, depth + 1)

            # 遍历父节点
            if node.val in fathers and fathers[node.val] != pre_node:
                find_ans(fathers[node.val], node, depth + 1)

        find_ans(target, '', 0)
        return ans
