#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 12:27
# @File    : PreorderTraversal.py
from typing import List

from datastructure.Stack.InorderTraversal import TreeNode


class PreorderTraversal(object):

    def __init__(self):
        pass

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        前序遍历，递归写法
        :param root:
        :return:
        """
        if not root:
            return []

        result = list()
        result.append(root.val)

        if root.left:
            result.extend(self.preorderTraversal(root.left))
        if root.right:
            result.extend(self.preorderTraversal(root.right))

        return result

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        迭代写法，使用栈，先压左子树，然后压根节点
        :param root:
        :return:
        """
        from collections import deque
        stack = deque()
        result = list()
        cur_node = root
        while stack or cur_node:
            while cur_node:
                result.append(cur_node.val)
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            cur_node = cur_node.right

        return result
