#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/17 13:49
# @File    : SetZeroes.py

"""

"""
from typing import List


class SetZeroes(object):

    def __init__(self):
        pass

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 使用set 记录 col、 row位置，空间复杂度N+M, 时间复杂度0(2 * N * M)
        col_set = set()
        row_set = set()

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in range(n):
            for j in range(m):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 使用第一行，第一列作为基准
        # 第一行是否有0
        row_flag = False
        # 第一列是否有0
        col_flag = False
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] == 0:
                col_flag = True
                break

        for j in range(m):
            if matrix[0][j] == 0:
                row_flag = True
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col_flag:
            for i in range(n):
                matrix[i][0] = 0

        if row_flag:
            for j in range(m):
                matrix[0][j] = 0