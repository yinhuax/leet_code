#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/17 23:02
# @File    : IsLandsNum.py
from typing import List
from collections import deque


class IsLandsNum(object):

    def __init__(self):
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        if len(grid) == 0 or not grid[0]:
            return num
        row = len(grid)
        col = len(grid[0])

        def bfs(i, j):
            # 可以往四个方向广搜
            queue = deque()
            queue.append((i, j))

            grid[i][j] = '2'

            while len(queue) > 0:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    for step in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        temp_i = curr[0] + step[0]
                        temp_j = curr[1] + step[1]
                        if 0 <= temp_i < row and 0 <= temp_j < col and grid[temp_i][temp_j] == '1':
                            grid[temp_i][temp_j] = '2'
                            queue.append((temp_i, temp_j))

            return 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    num += bfs(i, j)

        return num
