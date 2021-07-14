#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 22:23
# @File    : MinimumTotal.py
from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        类似杨辉三角，当前节点只有2个状态，1. 上个下标的i 或者 i - 1， 取和小的那个
        :param triangle:
        :return:
        """
        dp = [0] * len(triangle)
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
            dp[0] += triangle[i][0]

        return min(dp)


if __name__ == '__main__':
    print(Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
