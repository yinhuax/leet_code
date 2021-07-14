#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 15:51
# @File    : BuildTree2.py
from typing import List

from datastructure.binary_tree import TreeNode


class BuildTree2(object):

    def __init__(self):
        pass

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        复制数组方式
        :param preorder:
        :param inorder:
        :return:
        """
        assert len(preorder) == len(inorder)

        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])

        return root

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        计算下标方式
        :param preorder:
        :param inorder:
        :return:
        """

        def my_buildTree(p_start, p_end, i_start, i_end):
            if p_start > p_end or i_start > i_end:
                return None

            pos = inorder.index(preorder[p_start])
            root = TreeNode(inorder[pos])
            length = pos - i_start

            root.left = my_buildTree(p_start + 1, p_start + length, i_start, pos - 1)
            root.right = my_buildTree(p_start + length + 1, p_end, pos + 1, i_end)

            return root

        return my_buildTree(0, len(preorder) - 1, 0, len(inorder) - 1)
