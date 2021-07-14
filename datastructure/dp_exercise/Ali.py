#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/16 20:43
# @File    : Ali.py
"""

大概意思就是给定一个mXn的矩阵，矩阵里面都是非负整数，那么现在要从蓝色区域出发
（矩阵上边的矩阵外的区域），要到达红色区域，请问这个过程中的路径和最小是多少？
你可以从第一行任意一个起点出发，行走的时候可以 往下走，往左走，往右走。求最小的路径和。
（忘了加个条件，矩阵里都是非负数）需要遍历，
"""


class Ali(object):

    def min_path(self, matrix):
        """
        dp写法
        状态转移方程
        dp[i][j] = min(dp[i][j - 1], dp[i][j + 1], dp[i - 1][j]) + matrix[i][j]
        :param matrix:
        :return:
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化dp数组
        for i in range(m):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

            for j in range(m - 1, -1, -1):
                if j != m - 1:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i][j + 1])

        return min(dp[-1])


if __name__ == '__main__':
    matrix = [[100, 100, 100, 100, 1, 100, 100],
              [100, 1, 1, 1, 1, 100, 100],
              [100, 3, 2, 2, 100, 100, 100],
              [100, 100, 100, 3, 1, 100, 100]]
    print(Ali().min_path(matrix))
