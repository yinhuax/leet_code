#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/22 6:50
# @File    : IsToeplitzMatrix.py
from typing import List

"""
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/toeplitz-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        先遍历行，然后遍历列
        :param matrix:
        :return:
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            seen_set = set()
            tmp_i = i
            tmp_j = 0
            seen_set.add(matrix[tmp_i][tmp_j])
            while tmp_i < n - 1 and tmp_j < m - 1:
                tmp_i += 1
                tmp_j += 1
                seen_set.add(matrix[tmp_i][tmp_j])

                if len(seen_set) > 1:
                    return False

        for j in range(1, m):
            seen_set = set()
            tmp_i = 0
            tmp_j = j
            seen_set.add(matrix[tmp_i][tmp_j])
            while tmp_i < n - 1 and tmp_j < m - 1:
                tmp_i += 1
                tmp_j += 1
                seen_set.add(matrix[tmp_i][tmp_j])

                if len(seen_set) > 1:
                    return False

        return True

    def isToeplitzMatrix1(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            if matrix[i][1:] != matrix[i - 1][:-1]:
                return False
        return True

    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


if __name__ == '__main__':
    print(Solution().isToeplitzMatrix2([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
