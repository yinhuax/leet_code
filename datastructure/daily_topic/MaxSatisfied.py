#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/23 22:09
# @File    : MaxSatisfied.py
from typing import List

"""
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """
        滑动窗口
        :param customers:
        :param grumpy:
        :param X:
        :return:
        """
        # 1. 计算使用秘密技巧时，满意度总和
        total = 0
        for num, g in zip(customers, grumpy):
            if not g:
                total += num

        # 计算前X窗口使用秘密武器最大满意度
        satisfied = 0
        for i in range(X):
            if grumpy[i]:
                satisfied += customers[i]

        # 滑动窗口，计算最大满意度
        max_satisfied = satisfied
        for i in range(X, len(customers)):
            if grumpy[i - X]:
                satisfied -= customers[i - X]

            if grumpy[i]:
                satisfied += customers[i]

            max_satisfied = max(max_satisfied, satisfied)

        return max_satisfied + total


if __name__ == '__main__':
    print(Solution().maxSatisfied(customers=[3], grumpy=[1], X=1))
