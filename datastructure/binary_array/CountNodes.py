#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/29 13:45
# @File    : CountNodes.py

"""
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        """
        爆搜方式，使用层次遍历
        :param root:
        :return:
        """
        if not root:
            return 0

        from collections import deque
        q = deque()
        q.appendleft(root)

        n = 0
        while q:
            for _ in range(len(q)):
                cur_node = q.pop()
                n += 1
                if cur_node.left:
                    q.appendleft(cur_node.left)
                if cur_node.right:
                    q.appendleft(cur_node.right)

        return n

    def countNodes1(self, root: TreeNode) -> int:
        """
        使用递归方式
        :param root:
        :return:
        """
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return left + right + 1

    def countNodes2(self, root: TreeNode) -> int:
        """
        利用完全二叉树特性，先获得最大层数
        :param root:
        :return:
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        level = 0
        cur_node = root
        while cur_node:
            cur_node = cur_node.left
            level += 1

        # 定义左右边界
        # 完全二叉树，只有最后一层节点会为空，倒数第二层，判断下个节点是否为空
        left = 0
        maximum = 2 ** (level - 1) - 1
        right = maximum

        def search(num):
            turns = ('0' * (level - 1) + bin(num)[2:])[-(level - 1):]  # 这里是为了补位
            cur = root
            for turn in turns:
                if turn == '0':
                    cur = cur.left
                else:
                    cur = cur.right
            return True if cur else False

        while left <= right:
            mid = (left + right) >> 1
            if search(mid):
                left = mid + 1
            else:
                right = mid - 1

        # 如果是边界的话
        return left + maximum
