#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/12 12:47
# @File    : PrefixSum.py

"""
矩阵前缀和模板
"""


class MatrixPrefixSum(object):

    def __init__(self):
        pass

    def prefix_sum(self, matrix, x1, x2, y1, y2):
        """
        前缀和，输入一个数组，[l, r]，输出从l 到 r的和
        :param matrix:
        :param x1:
        :param x2:
        :param y1:
        :param y2:
        :return:
        """
        # 如果输入数组为空，特判
        if not matrix:
            return 0

        # 预留边界，减少判断 # TODO: 注意 初始化二维数组时，避免使用[[0] * n] * m 方式初始化， 会导致引用问题
        sums = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        # 初始化前缀和数组，使得S[i][j]为 (i, j) 左上部分所以元素和，S[i][j] = S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1] + matrix[i][j]，画图理解
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sums[i + 1][j + 1] = matrix[i][j] + sums[i + 1][j] + sums[i][j + 1] - sums[i][j]

        # 返回区间和， 同理以(x1, y1) 为左上角，(x2, y2) 为右下角的子矩阵和为S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1] + S[y1 - 1]
        # 因为S预留了边界，所以这里统一多移动一位，预留边界好处，边界值不需要特判如(0, 0)
        return sums[x2 + 1][y2 + 1] - sums[x1][y2 + 1] - sums[x2 + 1][y1] + sums[x1][y1]


if __name__ == '__main__':
    print(MatrixPrefixSum().prefix_sum([[1, 2, 3, 4, 5, 6],
                                        [7, 8, 9, 10, 11, 12],
                                        [13, 14, 15, 16, 17, 18],
                                        [19, 20, 21, 22, 23, 24],
                                        [25, 26, 27, 28, 29, 30],
                                        [31, 32, 33, 34, 35, 36]], 0, 5, 0, 5))
