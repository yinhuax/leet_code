#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 22:26
# @File    : SumNumbers.py
"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        dfs 深度优先遍历，存储从根节点到叶子节点的所有路径
        :param root:
        :return:
        """
        res = []

        def dfs(node, nums):
            if node:
                nums = nums * 10 + node.val
                if not node.left and not node.right:
                    res.append(nums)
                    return

                dfs(node.left, nums)
                dfs(node.right, nums)

        dfs(root, 0)
        print(res)
        return sum(res)


if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root1.left = root2
    root1.right = root3
    print(Solution().sumNumbers(root1))
