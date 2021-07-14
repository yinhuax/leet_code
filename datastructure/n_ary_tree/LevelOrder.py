#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 9:11
# @File    : LevelOrder.py
from typing import List

"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        # 层次遍历，广度优先遍历，使用队列
        from collections import deque
        queue = deque()
        queue.append(root)

        result = []
        while queue:
            res = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                res.append(cur_node.val)
                for child in cur_node.children:
                    queue.append(child)
            result.append(res)

        return result
