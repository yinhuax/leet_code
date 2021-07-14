#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/4 0:14
# @File    : FindDuplicateSubtrees.py
from typing import List

from datastructure.binary_tree import TreeNode


class FindDuplicateSubtrees(object):

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        使用前序遍历深搜+序列化树，使用哈希表存储出现次数
        :param root:
        :return:
        """
        hash_map = dict()
        result = list()

        def preorder(node):
            if not node:
                return '#'
            tree_ser = f'{node.val},{preorder(node.left)},{preorder(node.right)}'
            hash_map.setdefault(tree_ser, 0)
            hash_map[tree_ser] += 1
            if hash_map[tree_ser] == 2:
                result.append(node)
            return tree_ser

        preorder(root)
        return result
