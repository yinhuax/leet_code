#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/25 7:55
# @File    : Transpose.py
from typing import List

"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
"""


class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        行列转置
        :param matrix:
        :return:
        """
        n = len(matrix)
        m = len(matrix[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][i] = matrix[i][j]

        return result


if __name__ == '__main__':
    print(Solution().transpose(matrix=[[1, 2, 3], [4, 5, 6]]))
