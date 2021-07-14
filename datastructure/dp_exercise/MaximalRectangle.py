#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 18:32
# @File    : MaximalRectangle.py

"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""
from typing import List


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        前缀和 + 单调栈
        :param matrix:
        :return:
        """
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 1)

        ans = 0
        for i in range(row):
            for j in range(col):
                # 如果当前值为1，高度累加
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # 单调栈遍历，求最大面积
            stack = [-1]
            for k, num in enumerate(height):
                while stack and height[stack[-1]] > num:
                    pre_index = stack.pop()
                    ans = max(ans, (k - stack[-1] - 1) * height[pre_index])
                stack.append(k)

        return ans


if __name__ == '__main__':
    print(Solution().maximalRectangle(
        matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]))
