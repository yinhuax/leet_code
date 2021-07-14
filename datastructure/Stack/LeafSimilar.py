#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 8:58
# @File    : LeafSimilar.py

"""
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。



举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/leaf-similar-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        深度优先遍历
        :param root1:
        :param root2:
        :return:
        """

        def dfs(node, leaf_list):
            if not node:
                return

            if node and not node.left and not node.right:
                leaf_list.append(node.val)
                return

            dfs(node.left, leaf_list)
            dfs(node.right, leaf_list)

        leaf_list1 = []
        leaf_list2 = []
        dfs(root1, leaf_list1)
        dfs(root2, leaf_list2)

        return leaf_list1 and leaf_list2 and leaf_list1 == leaf_list2

    def leafSimilar1(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val

                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(1)
    print(Solution().leafSimilar(root1, root2))
