#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 22:13
# @File    : MaxProfit6.py
from typing import List

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        动态规划:
        dp[i][j]  i表示第i天，j表示持有未持有

        dp[i][0]  表示第i天未持有股票的情况, 一共两种情况:
            1. 昨天未持有，今天未持有
            2. 昨天持有，今天未持有，卖出需要手续费
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)

        dp[i][1]  表示第i天持有股票的情况，一共两种情况:
            1. 昨天持有，今天持有
            2. 昨天未持有，今天持有
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        :param prices:
        :param fee:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        """
        空间优化
        :param prices:
        :param fee:
        :return:
        """
        if len(prices) < 2:
            return 0

        profit_0 = 0
        profit_1 = -prices[0]
        for i in range(1, len(prices)):
            cur_price0 = max(profit_0, profit_1 + prices[i] - fee)
            cur_price1 = max(profit_1, profit_0 - prices[i])
            profit_0 = cur_price0
            profit_1 = cur_price1

        return profit_0


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
