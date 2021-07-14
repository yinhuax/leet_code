#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 21:44
# @File    : ClimbStairs.py


class ClimbStairs(object):

    def __init__(self):
        pass

    def climbStairs(self, n: int) -> int:
        """
        动态规划，一共两种状态，1，2， 初始化为dp[1] = 1, dp[2] = 2
        :param n:
        :return:
        """
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
