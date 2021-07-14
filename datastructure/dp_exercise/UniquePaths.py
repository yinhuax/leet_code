#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 14:07
# @File    : UniquePaths.py
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        动态规划， 空间复杂度O(M * N) 时间复杂度O(M * N)
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        :param m:
        :param n:
        :return:
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp)
        return dp[-1][-1]

    def uniquePaths1(self, m: int, n: int) -> int:
        """
        根据观察，当前坐标的值只与左边和上面的值相关，和其他无关
        :param m:
        :param n:
        :return:
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths1(m=3, n=7))
