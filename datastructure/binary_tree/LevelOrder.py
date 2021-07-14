#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 13:27
# @File    : LevelOrder.py
from typing import List

from datastructure.binary_tree import TreeNode


class LevelOrder(object):

    def __init__(self):
        pass

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        层序遍历
        :param root:
        :return:
        """
        # 使用队列
        from collections import deque
        result = []
        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            cur_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(cur_res)
        return result
