#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/18 7:21
# @File    : NumIslands.py
from typing import List

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
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

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1

    def get_count(self):
        return self.count

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.count += 1


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        并查集方式，计算岛屿数量
        :param grid:
        :return:
        """
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])

        uf = UnionFind()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    uf.add(i * col + j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        tmp_x = x + i
                        tmp_y = y + j
                        if 0 <= tmp_x < row and 0 <= tmp_y < col and grid[tmp_x][tmp_y] == '1':
                            uf.merge(i * col + j, tmp_x * col + tmp_y)

        return uf.get_count()


if __name__ == '__main__':
    print(Solution().numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
