#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/12 20:11
# @File    : DifferenceNum.py

"""
差分矩阵
"""


class DifferenceNum(object):

    def __init__(self):
        pass

    def insert(self, b_arr, x1, y1, x2, y2, c):
        # 画图理解
        b_arr[x1][y1] += c
        b_arr[x1][y2 + 1] -= c
        b_arr[x2 + 1][y1] -= c
        b_arr[x2 + 1][y2 + 1] += c

    def diff_num(self, matrix, add_arr):
        """
        前缀和逆运算， 快速给区间 加上指定值
        :param matrix:
        :param add_arr:
        :return:
        """
        import numpy as np

        # 预留边界，减少判断 # TODO: 注意 初始化二维数组时，避免使用[[0] * n] * m 方式初始化， 会导致引用问题，或者使用np创建
        # b_arr = [[0 for _ in range(len(matrix[0]) + 2)] for _ in range(len(matrix) + 2)]
        b_arr = np.zeros([len(matrix) + 2, len(matrix[0]) + 2])
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.insert(b_arr, i, j, i, j, matrix[i - 1][j - 1])

        # 插入l, r, c
        for x1, y1, x2, y2, c in add_arr:
            self.insert(b_arr, x1, y1, x2, y2, c)

        # 重新计算二维前缀和
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                b_arr[i][j] += b_arr[i][j - 1] + b_arr[i - 1][j] - b_arr[i - 1][j - 1]

        return b_arr[1:-1, 1:-1]


if __name__ == '__main__':
    print(DifferenceNum().diff_num([[1, 2, 2, 1],
                                    [3, 2, 2, 1],
                                    [1, 1, 1, 1]], [[1, 1, 2, 2, 1], [1, 3, 2, 3, 2], [3, 1, 3, 4, 1]]))
