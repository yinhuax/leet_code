#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 21:21
# @File    : MaxProfit5.py
from typing import List

"""
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        动态规划
        方程为 dp[i][k][j]  0 <= i < len(prices)  表示天数
        dp[i][k][0] 表示当前天未持股，有以下两种情况:
                1. 昨天未持股今天也未持股
                2. 昨天持股，今天卖出
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])

        dp[i][k][1] 表示当前天持股，有以下两种情况:
                1. 昨天持股，今天也持股
                2. 昨天未持股，今天买入
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        :param k:
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(len(prices))]
        for i in range(1, k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]

    def maxProfit1(self, k: int, prices: List[int]) -> int:
        """
        空间优化，
        注意到第i天的最大收益，只与i - 1天最大收益相关，空间复杂度可以降低为O(k)
        :param k:
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])

        return dp[-1][0]


if __name__ == '__main__':
    print(Solution().maxProfit1(k=2, prices=[2, 4, 1]))
