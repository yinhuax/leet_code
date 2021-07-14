#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 18:09
# @File    : InsertIntoBST.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        遍历方式，找到合适的叶子节点，插入
        :param root:
        :param val:
        :return:
        """
        if not root:
            return TreeNode(val)

        cur_node = root
        pre_node = root
        while cur_node:
            pre_node = cur_node
            if cur_node.val < val:
                # 从右子树找
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

        new_node = TreeNode(val)
        if pre_node.val > val:
            pre_node.left = new_node
        else:
            pre_node.right = new_node

        return root

    def insertIntoBST1(self, root: TreeNode, val: int) -> TreeNode:
        """
        递归算法
        :param root:
        :param val:
        :return:
        """
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


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
    print(Solution().insertIntoBST1(t1, 5))
