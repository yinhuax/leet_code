#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 17:36
# @File    : SearchBST.py
"""
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        递归搜索
        :param root:
        :param val:
        :return:
        """
        cur_node = root
        while cur_node:
            if cur_node.val == val:
                return cur_node
            elif cur_node.val > val:
                # 当前值大于指定值，从左子树找
                cur_node = cur_node.left
            else:
                # 从右子树找
                cur_node = cur_node.right

        return None


if __name__ == '__main__':
    t1 = TreeNode(4)
    t2 = TreeNode(2)
    t3 = TreeNode(1)
    t4 = TreeNode(3)
    t5 = TreeNode(7)

    t1.left = t2
    t1.right = t5

    t2.left = t3
    t2.right = t4

    print(Solution().searchBST(t1, 5).val)
