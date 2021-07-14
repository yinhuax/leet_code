#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/19 17:42
# @File    : NumIslands.py
from typing import List


class NumIslands(object):

    def __init__(self):
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if row < 1 or col < 1:
            return 0

        def dfs(i, j):
            grid[i][j] = '0'

            for r, c in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                temp_i = i + r
                temp_j = j + c
                if 0 <= temp_i < row and 0 <= temp_j < col and grid[temp_i][temp_j] == '1':
                    dfs(temp_i, temp_j)
            return 1

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += dfs(i, j)

        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(NumIslands().numIslands(grid))

