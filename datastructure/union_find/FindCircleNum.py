#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/18 7:47
# @File    : FindCircleNum.py
from typing import List

"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.count += 1

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        并查集，或者dfs
        :param isConnected:
        :return:
        """
        if not isConnected or not isConnected[0]:
            return 0
        # 构建并查集
        row = len(isConnected)
        col = len(isConnected[0])
        uf = UnionFind()
        for i in range(row):
            for j in range(col):
                if isConnected[i][j]:
                    uf.add(i)
                    uf.add(j)
                    uf.merge(i, j)

        return uf.count


if __name__ == '__main__':
    print(Solution().findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
