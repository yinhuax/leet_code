#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/4 16:48
# @File    : RecoverFromPreorder.py
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        深度优先遍历，因为先序遍历顺序为根左右， 所以用list可以保存当前层从左到右的顺序
        :param traversal:
        :return:
        """
        if not traversal:
            return Optional.empty()

        from collections import defaultdict
        tree_table = defaultdict(list)
        level, num = 0, 0

        n = len(traversal)

        for s, i in enumerate(traversal):
            if s == '-':
                level += 1
            else:
                num = num * 10 + int(traversal[i])
                if i == n - 1 or traversal[i + 1] == '-':
                    # 数字结尾
                    # 开始构建树
                    cur_node = TreeNode(num)
                    tree_table[level].append(cur_node)
                    # 连接到父结点上
                    if tree_table[level - 1]:
                        if tree_table[level - 1][-1].left:
                            tree_table[level - 1][-1].right = cur_node
                        else:
                            tree_table[level - 1][-1].left = cur_node

                    level = num = 0

        return tree_table[0][0]
