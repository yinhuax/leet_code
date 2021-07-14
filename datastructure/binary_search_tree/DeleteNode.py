#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 21:22
# @File    : DeleteNode.py
"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/introduction-to-data-structure-binary-search-tree/xpcnds/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DeleteNode(object):

    def __init__(self):
        pass

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        删除节点分为三种情况:
        1. 当前节点为叶子节点，直接删除
        2. 当前节点有叶子节点，使用叶子节点替换
            1. 如果有右节点，使用后续节点替换，后续节点为先取右叶子节点，然后一直取左叶子节点
            2. 如果没有右节点，使用前续节点替换，前序节点为先取左叶子节点，然后一直取右叶子节点
        :param root:
        :param key:
        :return:
        """
        if not root:
            return None

        if key > root.val:
            # 从右子树删除
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # 从左子树删除
            root.left = self.deleteNode(root.left, key)
        else:
            # 判断是否是叶子节点
            if not root.left and not root.right:
                root = None
            elif root.right:
                # 判断右节点是否存在
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
