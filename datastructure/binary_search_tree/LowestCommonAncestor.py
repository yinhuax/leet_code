#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 21:51
# @File    : LowestCommonAncestor.py
"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/introduction-to-data-structure-binary-search-tree/xpf523/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestor(object):

    def __init__(self):
        pass

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        最近公共祖先
        :param root:
        :param p:
        :param q:
        :return:
        """
        # 判断是否为公共祖先，只需要满足 (p.val < root.val > q.val) or (p.val > root.val and q.val > root.val) 两个条件不成立
        ancestor = root
        while True:
            if p.val < ancestor.val > q.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break

        return ancestor

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        两次遍历写法
        :param root:
        :param p:
        :param q:
        :return:
        """

        # 存储中序遍历路径，找到公共祖先
        def dfs(root, path, q):
            if not root:
                return False

            path.append(root)
            if root == q:
                return True

            ret = dfs(root.left, path, q)
            if not ret:
                ret = dfs(root.right, path, q)

            if not ret:
                path.pop()

            return ret

        p_path = []
        q_path = []
        dfs(root, p_path, p)
        dfs(root, q_path, q)

        # 遍历找到最后一个相同的节点
        ancestor = None
        for u, v in zip(p_path, q_path):
            if u == v:
                ancestor = u
            else:
                break

        return ancestor
