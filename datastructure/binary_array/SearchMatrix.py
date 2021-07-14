#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/5 23:01
# @File    : SearchMatrix.py
from typing import List

"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        搜索二维矩阵
        :param matrix:
        :param target:
        :return:
        """
        row = len(matrix)
        if row < 1:
            return False
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            mid = left + (right - left) // 2
            cur_row = mid // col
            cur_col = mid % col
            if matrix[cur_row][cur_col] == target:
                return True
            elif matrix[cur_row][cur_col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
