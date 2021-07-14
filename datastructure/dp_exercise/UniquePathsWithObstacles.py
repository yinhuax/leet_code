#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 14:29
# @File    : UniquePathsWithObstacles.py
from typing import List

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        动态规划：
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        如果是障碍物 dp[i][j] = 0
        :param obstacleGrid:
        :return:
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化值，如果遇到obstacleGrid[i][j] == 1 跳出循环
        for i in range(n):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1

        for j in range(m):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        """
        空间优化
        :param obstacleGrid:
        :return:
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [0] * m

        dp[0] = 0 if obstacleGrid[0][0] else 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j >= 1 and not obstacleGrid[i][j]:
                    dp[j] += dp[j - 1]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles1([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
