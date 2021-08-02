#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/2 7:51
# @File    : SearchMatrix2.py
from typing import List

"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        二分查找法
        :param matrix:
        :param target:
        :return:
        """
        col = len(matrix[0])
        for line in matrix:
            # 判断target是否位于当前行
            if line[0] <= target <= line[col - 1]:
                # 查找当前行
                if self.binary_search(line, target):
                    return True

        return False

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """
        特殊遍历方式，利用矩阵特性， 从右上角或者左下角开始遍历
        :param matrix:
        :param target:
        :return:
        """
        # 从右上角开始遍历
        row = len(matrix)
        col = len(matrix[0])

        r = 0
        c = col - 1
        while 0 <= r < row and 0 <= c < col:
            # 小于往下走
            if matrix[r][c] < target:
                r += 1
            # 大于往左走
            elif matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] == target:
                return True

        return False


if __name__ == '__main__':
    matrix = [[-5]]
    target = -5

    print(Solution().searchMatrix1(matrix, target))
