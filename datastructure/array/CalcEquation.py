#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/16 18:04
# @File    : CalcEquation.py
from typing import List

"""
并查集



给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 
共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
"""

"""
手写并查集
"""


class UnionFind(object):

    def __init__(self):
        """
        记录每个节点的父结点
        记录每个节点到根节点的权重
        """
        self.father = {}
        self.value = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        :param x:
        :return:
        """
        root = x
        # 节点更新权重的时候要放大的倍数
        base = 1
        while self.father[root]:
            root = self.father[root]
            base *= self.value[root]

        while x != root:
            origin_father = self.father[x]
            # 离根节点越远，放大的倍数越高
            self.value[x] *= base
            base /= self.value[origin_father]
            self.father[x] = root
            x = origin_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        :param x:
        :param y:
        :param val:
        :return:
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 四边形法则更新根节点的权重
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        """
        两节点是否相连
        :param x:
        :param y:
        :return:
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点，初始化权重为1.0
        :param x:
        :return:
        """
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        uf = UnionFind()
        # 构建并查集
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)

        print(uf.value)
        print(uf.father)
        res = [-1.0] * len(queries)

        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                res[i] = uf.value[a] / uf.value[b]

        return res


if __name__ == '__main__':
    print(Solution().calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                  queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
