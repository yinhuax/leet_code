#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 17:27
# @File    : MaxProfit4.py
from typing import List

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划：
        dp[i][0] 表示第i天 未持有股票，dp[i][1] 表示第i天 持有股票

        dp[i][0] 未持有并冻结股票有2种情况：
            1. 昨天未持有，今天未持有
            2. 昨天持有，今天卖出
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

        dp[i][1] 持有股票有2种情况:
            1. 昨天持有，今天继续持有
            2. 前天未持有，今天买入
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i])

        dp[i][2] 未持有股票并未冻结的情况:
            1. 昨天未持有但被冻结
            2. 昨天未持有但未被冻结
            dp[]
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][2] - prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][0])

        return max(dp[-1][0], dp[-1][2])

    def maxProfit1(self, prices: List[int]) -> int:
        """
        使用n * 2维数组 优化空间
        :param prices:
        :return:
        """

        if len(prices) < 2:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i] if i > 2 else -prices[i])

        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        """
        优化空间，发现第i天的收益，之和第i - 1天，第i - 2天最大收益相关，空间复杂度降到O(1)
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        # 表示卖出
        profit_0 = 0
        # 表示买入
        profit_1 = -prices[0]
        # 表示冻结
        pre_profit = 0
        for i in range(1, len(prices)):
            # 未持有状态，上次未持有，或者上次持有当日卖出
            next_profit0 = max(profit_0, profit_1 + prices[i])
            # 持有状态，上次持有，或者上上次冻结未持有买入
            next_profit1 = max(profit_1, pre_profit - prices[i])
            # 存储上次买出未持有时最大收益
            pre_profit = profit_0
            profit_0 = next_profit0
            profit_1 = next_profit1

        return max(profit_0, pre_profit)


if __name__ == '__main__':
    print(Solution().maxProfit2([1, 2, 3, 0, 2]))
