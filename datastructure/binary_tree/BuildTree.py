#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 14:49
# @File    : BuildTree.py
from typing import List

from datastructure.binary_tree import TreeNode


class BuildTree(object):

    def __init__(self):
        pass

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        数组赋值方式，简单，但是时间复杂度高
        :param inorder:
        :param postorder:
        :return:
        """
        assert len(inorder) == len(postorder)

        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:pos], postorder[:pos])

        root.right = self.buildTree(inorder[pos + 1:], postorder[pos:-1])

        return root

    def buildTree1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        计算下标方式，使用左右子树在中序，后序遍历中长度一致原理，计算下标
        :param inorder:
        :param postorder:
        :return:
        """

        def my_buildTree(i_start, i_end, p_start, p_end):
            if i_start > i_end or p_start > p_end:
                return None

            if i_start == i_end or p_start == p_end:
                return TreeNode(inorder[i_start])

            node = TreeNode(postorder[p_end])
            pos = inorder.index(postorder[p_end])

            node.left = my_buildTree(i_start, pos - 1, p_start, p_start + (pos - 1 - i_start))
            node.right = my_buildTree(pos + 1, i_end, p_start + (pos - 1 - i_start) + 1, p_end - 1)

            return node

        return my_buildTree(0, len(inorder) - 1, 0, len(postorder) - 1)
