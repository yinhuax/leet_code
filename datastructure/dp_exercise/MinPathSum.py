#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 16:08
# @File    : MinPathSum.py
from typing import List

"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
"""


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        动态规划

        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        :param grid:
        :return:
        """
        n = len(grid)
        m = len(grid[0])

        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = grid[i][0]
            else:
                dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(m):
            if j == 0:
                dp[0][j] = grid[j][0]
            else:
                dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]

    def minPathSum1(self, grid: List[List[int]]) -> int:
        """
        不使用额外空间
        :param grid:
        :return:
        """
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


if __name__ == '__main__':
    print(Solution().minPathSum1(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
