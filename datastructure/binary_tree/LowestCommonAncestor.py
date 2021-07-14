#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 18:22
# @File    : LowestCommonAncestor.py

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestor(object):

    def __init__(self):
        pass

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        递归方式，寻找最近公共祖先
        :param root:
        :param p:
        :param q:
        :return:
        """
        """
        深度遍历优先，使用列表存储路径
        """

        # 深度搜索两个子节点的路径
        def dfs(root, target, lists):
            if not root:
                return False

            lists.append(root)
            if root == target:
                return True

            ret = dfs(root.left, target, lists)
            if not ret:
                ret = dfs(root.right, target, lists)
            if not ret:
                lists.pop()
            return ret

        # 获得两个节点的路径
        p_paths = []
        q_paths = []
        dfs(root, p, p_paths)
        dfs(root, q, q_paths)

        min_len = min(len(p_paths), len(q_paths))
        for i in range(min_len):
            if p_paths[i] != q_paths[i]:
                # 上个节点为公共节点
                return p_paths[i - 1]
        return p_paths[min_len - 1] if len(p_paths) > len(q_paths) else q_paths[min_len - 1]

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        二叉树的最近公共祖先
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root or root == p or root == q:
            return root

        # 后序遍历方式
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左子树和右子树都能找到，那么当前root就是最近公共祖先
        if left and right:
            return root
        # 如果左子树找到，右子树找不到，那么左子树为最近公共祖先
        if left:
            return left
        if right:
            return right

        return None


if __name__ == '__main__':
    root = TreeNode(3)
    p1 = TreeNode(5)
    p2 = TreeNode(1)
    p3 = TreeNode(6)
    p4 = TreeNode(2)
    p5 = TreeNode(0)
    p7 = TreeNode(8)
    p8 = TreeNode(7)
    p9 = TreeNode(4)

    root.left = p1
    root.right = p2
    p1.left = p3
    p1.right = p4
    p2.left = p5
    p2.right = p7
    p4.left = p8
    p4.right = p9

    print(LowestCommonAncestor().lowestCommonAncestor(root, p1, p9).val)
