#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 23:28
# @File    : LargestSumOfAverages.py
from typing import List

"""
我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-sum-of-averages
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        动态规划：
        dp[i][j]  表示 前i个数分割为j段 最大的平均数
        dp[i][j] = max(dp[i][j], dp[k][j - 1] + sub(k + 1, i) / ( k + 1 - i))
        :param A:
        :param K:
        :return:
        """
        # 前缀和计算
        sums = [0] * (len(A) + 1)
        for i in range(len(A)):
            if i == 0:
                sums[i + 1] = A[i]
            sums[i + 1] = sums[i] + A[i]

        # 初始化dp数组
        dp = [[0 for _ in range(K + 1)] for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):  # 枚举每个子数组末尾
            dp[i][1] = sums[i] / i
            for j in range(2, min(i, K) + 1):  # 枚举子数组的拆分次数
                for k in range(1, i):  # 枚举每个拆分位置
                    dp[i][j] = max(dp[i][j], dp[k][j - 1] + ((sums[i] - sums[k]) / (i - k)))

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().largestSumOfAverages(A=[9, 1, 2, 3, 9], K=3))
