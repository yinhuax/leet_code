#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 16:55
# @File    : IsValidBST.py
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/introduction-to-data-structure-binary-search-tree/xpkc6i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        递归，中序遍历，验证是否是有效的二叉搜索树。
        :param root:
        :return:
        """

        def dfs(root: TreeNode, left, right) -> bool:
            if not root:
                return True

            if left < root.val < right:
                return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            else:
                return False

        return dfs(root, -float('inf'), float('inf'))


if __name__ == '__main__':
    pass
