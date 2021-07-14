#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 19:48
# @File    : MaximalSquare.py
from typing import List

"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

 
"""


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        动态规划
        1. 如果 matrix[i][j] == 0  dp[i][j] = 0
        2. 如果 matrix[i][j] == 1  当前位置需要比较左边、上面、左上三个位置的值
            转移方程为 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        :param matrix:
        :return:
        """
        n = len(matrix)
        m = len(matrix[0])

        max_side = 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side ** 2


if __name__ == '__main__':
    print(Solution().maximalSquare([["0", "1"], ["1", "0"]]))
