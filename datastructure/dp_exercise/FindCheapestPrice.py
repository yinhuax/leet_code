#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/29 5:47
# @File    : FindCheapestPrice.py
from typing import List

"""
有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 
src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        动态规划： fight = [src, dst, price]
                 递推方程： dp[k][dst] = min(dp[k][dst], dp[k - 1][src] + price)
        :param n:
        :param flights:
        :param src:
        :param dst:
        :param K:
        :return:
        """
        dp = [[float('inf')] * n for _ in range(K + 1)]

        for flight in flights:
            if flight[0] == src:
                dp[0][flight[1]] = flight[2]

        for k in range(K + 1):
            dp[k][src] = 0

        for k in range(1, K + 1):
            for flight in flights:
                if dp[k - 1][flight[0]] != float('inf'):
                    dp[k][flight[1]] = min(dp[k][flight[1]], dp[k - 1][flight[0]] + flight[2])

        return dp[K][dst] if dp[K][dst] != float('inf') else -1
