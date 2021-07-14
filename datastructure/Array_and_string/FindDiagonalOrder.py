#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/18 22:19
# @File    : FindDiagonalOrder.py
"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

LC 对角线遍历
"""
from typing import List


class FindDiagonalOrder(object):

    def __init__(self):
        pass

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        模拟题，规律是遍历时横坐标与纵坐标之和 = 遍历次数 - 1，遍历总次数 = m + n - 1
        :param matrix:
        :return:
        """
        # 设置tag判断是往右上走，还是往左下走，默认右上，往上走遍历行
        result = []
        if not matrix:
            return result

        flag = True
        row = len(matrix)
        col = len(matrix[0])

        for ix in range(row + col - 1):
            xMax = row if flag else col
            yMax = col if flag else row

            # for i in range(min(ix + 1, xMax)):
            #     counter += 1
            #     j = ix - i
            #     if j >= yMax:
            #         # 剪枝，去除边界外的值
            #         continue
            #
            #     result.append(matrix[i][j] if flag else matrix[j][i])

            i = min(ix, xMax - 1)
            j = ix - i
            while i >= 0 and j < yMax:
                result.append(matrix[i][j] if flag else matrix[j][i])
                i -= 1
                j += 1

            flag = not flag

        return result


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(FindDiagonalOrder().findDiagonalOrder(matrix))
