#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 20:16
# @File    : MaxSumSubmatrix.py
from typing import List

"""
给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

示例:

输入: matrix = [[1,0,1],[0,-2,3]], k = 2
输出: 2 
解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MaxSumSubmatrix(object):

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        动态规划， 超时

        动态规划转移方程为:
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1] 表示从原点到i, j的矩阵和

        遍历i， j 看dp[i][j] 中是否有满足 <= k 的最大值，扩散到整个矩阵就可以知道当前矩阵的最大值
        :param matrix:
        :param k:
        :return:
        """
        n = len(matrix)
        m = len(matrix[0])

        # 求最大值，使用-inf作为初始化值
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # 初始化默认值
        for i in range(n + 1):
            dp[i][0] = 0

        for j in range(m + 1):
            dp[0][j] = 0

        ans = float('-inf')
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 计算原点到当前点的矩阵面积
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
                for u in range(i):
                    for v in range(j):
                        temp = dp[i][j] - dp[u][j] - dp[i][v] + dp[u][v]
                        if temp <= k:
                            ans = max(ans, temp)

        return ans

    def maxSumSubmatrix1(self, matrix: List[List[int]], k: int) -> int:
        """
        前缀和 + 二分查找
        :param matrix:
        :param k:
        :return:
        """
        import bisect

        row = len(matrix)
        col = len(matrix[0])

        # 左边界
        res = float('-inf')
        for left in range(col):
            # 初始化nums，用来记录前缀和
            nums = [0] * row
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]

                # 在left， right为边界下的矩阵
                # 求不超过k的最大数值和
                # 用来存cum的array数组，已排序
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)
                    if loc < len(array):
                        res = max(res, cum - array[loc])

                    bisect.insort(array, cum)

        return res


if __name__ == '__main__':
    print(MaxSumSubmatrix().maxSumSubmatrix())
