#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/28 15:41
# @File    : MaxProfit.py
from typing import List

"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        暴力法，时间复杂度O(N)，空间复杂度O(1)
        :param prices:
        :return:
        """
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

    def maxProfit1(self, prices: List[int]) -> int:
        """
        动态规划写法:
        定义动态方程为dp[i][j]  i -> 第i天, j 持股状态

        定义j 为 0、1两种状态，0未持股，1持股：

        0 状态转移：
        前一天未持股，当前天未持股
        前一天持股，当前天未持股
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + price)

        1 状态转移：
        前一天未持股，当前天持股
        前一天持股，当前天持股

        只允许买卖一次，所以前天未持股，前天手上现金为0
        dp[i][1] = max(dp[i - 1][1], -price)

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
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        # 返回最后一天未持股状态
        return dp[-1][0]
