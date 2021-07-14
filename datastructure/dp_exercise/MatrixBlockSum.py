#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/29 6:16
# @File    : MatrixBlockSum.py
from typing import List

"""
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，
其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 


i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-block-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
        矩阵前缀和
        :param mat:
        :param K:
        :return:
        """
        row = len(mat)
        col = len(mat[0])

        P = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        # 重新计算矩阵前缀和
        result = [[0] * col for _ in range(row)]

        def get(x, y):
            x = max(min(x, row), 0)
            y = max(min(y, col), 0)
            return P[x][y]

        for i in range(row):
            for j in range(col):
                # 计算范围
                result[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(
                    i - K,
                    j - K)

        return result


if __name__ == '__main__':
    print(Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1))
