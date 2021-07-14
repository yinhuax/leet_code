#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/16 23:15
# @File    : Rotate.py
from typing import List


class Rotate(object):

    def __init__(self):
        pass

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
                    matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
                print(i, j)

    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        先按主对角线翻转，然后左右列交替
        :param matrix:
        :return:
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 左右列交替
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        逆时针翻转，先按负对角线翻转, 然后左右列交替
        :param matrix:
        :return:
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]

        # 左右列交替
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


if __name__ == '__main__':
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print(Rotate().rotate2(matrix))
    print(matrix)
