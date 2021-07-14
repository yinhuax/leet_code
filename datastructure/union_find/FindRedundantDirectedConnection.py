#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/19 7:43
# @File    : FindRedundantDirectedConnection.py
from typing import List

"""
在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。
该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。

输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。

返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def add(self, x):
        if x not in self.father:
            self.father[x] = x


class Solution:

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        有向图，需要判断是否存在环和冲突边

        环的优先级大于冲突边
        :param edges:
        :return:
        """
        uf = UnionFind()
        parent = list(range(len(edges) + 1))

        # 冲突/环标签
        conflict = -1
        cycle = -1

        # 开始遍历
        for i, (node1, node2) in enumerate(edges):
            uf.add(node1)
            uf.add(node2)

            if parent[node2] != node2:
                # 产生冲突，有两个父节点
                conflict = i
            else:
                parent[node2] = node1
                if uf.is_connected(node1, node2):
                    # 产生环
                    cycle = i
                else:
                    uf.merge(node1, node2)

        # 获取有问题的边
        if conflict < 0:
            # 没有冲突边，返回环
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflict_edge = edges[conflict]
            if cycle >= 0:
                # 环优先级比冲突大
                return [parent[conflict_edge[1]], conflict_edge[1]]
            else:
                return [conflict_edge[0], conflict_edge[1]]
