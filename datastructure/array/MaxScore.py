#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/27 16:43
# @File    : MaxScore.py
from typing import List

"""
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        转换思路，计算连续子数组最小值，长度为 len(cardPoints) - K
        :param cardPoints:
        :param k:
        :return:
        """
        n = len(cardPoints)
        window_size = n - k
        # 选择前n-k为初始化值
        s = sum(cardPoints[:window_size])
        min_sum = s
        for i in range(window_size, n):
            s += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, s)

        return sum(cardPoints) - min_sum
