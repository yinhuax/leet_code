#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 6:10
# @File    : IsBalanced.py
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IsBalanced(object):

    def isBalanced(self, root: TreeNode) -> bool:
        """

        :param root:
        :return:
        """

        def dfs(root):
            if not root:
                return 0

            return max(dfs(root.left), dfs(root.right)) + 1

        if not root:
            return True

        return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced1(self, root: TreeNode) -> bool:
        self.res = True

        def helper(root):
            if not root:
                return 0

            left = helper(root.left) + 1
            right = helper(root.right) + 1
            if abs(right - left) > 1:
                self.res = False

            return max(left, right)

        helper(root)
        return self.res


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    print(IsBalanced().isBalanced(t1))
