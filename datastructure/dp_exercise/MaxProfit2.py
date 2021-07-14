#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 11:49
# @File    : MaxProfit2.py
from typing import List

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划
        股票可以多次交易，在再次购买前需要出售掉之前的股票，同一天不能同时卖出买入
        以i表示天数，用0、1表示未持股 或者 持股状态，方程表示为dp[i][0]、dp[i][1]

        dp[i][0] 表示第i天未持股，分为两种情况:
                1. 昨天未持股，今天未持股
                2. 昨天持股，今天卖出
                方程表示为 dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

        dp[i][1] 表示第i天持股，分为两种情况
                1. 昨天未持股，今天买入
                2. 昨天持股，今天不动
                因为可以多次买卖，使用前面的利润减去今天买入的价格，为当前持有现金
                方程表示为 dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        最后一天需要抛掉所有股票，所以返回dp[-1][0]
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # 从第二天开始遍历
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

    def maxProfit1(self, prices: List[int]) -> int:
        """
        动态规划，优化空间
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            cur_cash = max(cash, hold + prices[i])
            cur_hold = max(hold, cash - prices[i])
            cash = cur_cash
            hold = cur_hold

        return cash


if __name__ == '__main__':
    print(Solution().maxProfit1([7, 1, 5, 3, 6, 4]))
