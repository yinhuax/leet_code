#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 14:21
# @File    : BuildTree.py
"""
给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
import pytest


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        使用前序与中序遍历序列构建二叉树
        :param preorder:
        :param inorder:
        :return:
        """
        if len(preorder) != len(inorder):
            raise ValueError("preorder and inorder is not the same length!!!")

        return self._buildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def _buildTree(self, preorder: List[int], preL, preR, inorder: List[int], inL, inR):
        if preL > preR or inL > inR:
            return None

        pivot = preorder[preL]
        pivot_index = inorder.index(pivot)

        root = TreeNode(pivot)
        root.left = self._buildTree(preorder, preL + 1,
                                    preL + pivot_index - inL,
                                    inorder, inL, pivot_index - 1)
        root.right = self._buildTree(preorder, preL + pivot_index - inL + 1,
                                     preR, inorder, pivot_index + 1, inR)

        return root
