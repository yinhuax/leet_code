#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 22:40
# @File    : RangeSumBST.py
"""

给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

 

示例 1：


输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-of-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        深度优先遍历
        :param root:
        :param low:
        :param high:
        :return:
        """
        self.res = 0

        def dfs(node):
            if not node:
                return

            self.res += node.val if low <= node.val <= high else 0
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res
