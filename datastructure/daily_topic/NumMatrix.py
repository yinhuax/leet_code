#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/2 23:41
# @File    : NumMatrix.py
from typing import List

"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        二维矩阵前缀和
        :param matrix:
        """
        self.matrix = matrix
        self.row = len(self.matrix)
        if self.row < 1:
            return
        self.col = len(self.matrix[0])

        # 计算行方向前缀和
        for i in range(1, self.row):
            self.matrix[i][0] += self.matrix[i - 1][0]
        # 计算列方向前缀和
        for j in range(1, self.col):
            self.matrix[0][j] += self.matrix[0][j - 1]

        for i in range(1, self.row):
            for j in range(1, self.col):
                self.matrix[i][j] += self.matrix[i - 1][j] + self.matrix[i][j - 1] - self.matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not (0 <= row1 < self.row and 0 <= col1 < self.col and 0 <= row2 < self.row and 0 <= col2 < self.col):
            return 0

        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        else:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2] + \
                   self.matrix[row1 - 1][col1 - 1]


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    print(NumMatrix(matrix).sumRegion(0, 0, 4, 4))
