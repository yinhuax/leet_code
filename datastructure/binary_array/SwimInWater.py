#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/4 22:36
# @File    : SwimInWater.py
from typing import List

"""
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，
但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swim-in-rising-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        二分查找，水位为min(grid), max(grid)，判断当前时间t，是否存在路径能到达最右下角
        :param grid:
        :return:
        """
        row = len(grid)
        col = len(grid[0])

        left, right = float('inf'), float('-inf')
        for i in range(row):
            for j in range(col):
                left = min(grid[i][j], left)
                right = max(grid[i][j], right)

        def dfs(x, y, visited, t):
            if x == row - 1 and y == col - 1:
                return True

            visited[x][y] = True
            for i, j in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and max(grid[x][y], grid[tmp_i][tmp_j]) <= t and not visited[tmp_i][tmp_j]:
                    if dfs(tmp_i, tmp_j, visited, t):
                        return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            visited = [[False for _ in range(col)] for _ in range(row)]
            # 从(0, 0)位置开始寻找
            if dfs(0, 0, visited, mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(Solution().swimInWater(
        [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
