#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 10:16
# @File    : MaxProfit.py
from typing import List

"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        最大股票收益
        dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
        dp[i][1] = max(dp[i - 1][1], -prices[i])
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
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        return dp[-1][0]

    def maxProfit1(self, prices: List[int]) -> int:
        """
        空间优化
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [0, 0]
        dp[0] = 0
        dp[1] = -prices[0]
        for i in range(1, len(prices)):
            dp[0] = max(dp[1] + prices[i], dp[0])
            dp[1] = max(dp[1], -prices[i])

        return dp[0]
