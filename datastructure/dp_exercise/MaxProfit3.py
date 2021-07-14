#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 15:09
# @File    : MaxProfit3.py
from typing import List

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划，构造状态转移方程
        dp[i][k][j] i表示天数，k表示买卖次数，j表示是持股还是未持股

        dp[i][k][0] 表示当前天未持股，有以下两种情况:
                1. 昨天未持股今天也未持股
                2. 昨天持股，今天卖出
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])

        dp[i][k][1] 表示当前天持股，有以下两种情况:
                1. 昨天持股，今天也持股
                2. 昨天未持股，今天买入
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k][0] - prices[i])
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [[[0 for _ in range(2)] for _ in range(3)] for i in range(len(prices))]

        for i in range(1, 3):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]

        for i in range(1, len(prices)):
            for k in range(2, 0, -1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[-1][2][0]

    def maxProfit1(self, prices: List[int]) -> int:
        """
        动态规划，构造状态转移方程
        dp[i][k][j] i表示天数，k表示买卖次数，j表示是持股还是未持股

        dp[i][k][0] 表示当前天未持股，有以下两种情况:
                1. 昨天未持股今天也未持股
                2. 昨天持股，今天卖出
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])

        dp[i][k][1] 表示当前天持股，有以下两种情况:
                1. 昨天持股，今天也持股
                2. 昨天未持股，今天买入
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k][0] - prices[i])
        :param prices:
        :return:
        """
        # 空间优化
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
