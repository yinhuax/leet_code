#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 17:22
# @File    : BSTIterator.py
"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root: TreeNode):
        """
        扁平处理，中序遍历获得数据
        :param root:
        """
        self.root = root
        self.inorder_list = []
        self.len = -1
        # 构建中序遍历结果
        self.build_iterator(self.root)

    def next(self) -> int:
        self.len += 1
        return self.inorder_list[self.len]
        pass

    def hasNext(self) -> bool:
        return self.len + 1 < len(self.inorder_list)

    def build_iterator(self, root):
        if not root:
            return

        self.build_iterator(root.left)
        self.inorder_list.append(root.val)
        self.build_iterator(root.right)
