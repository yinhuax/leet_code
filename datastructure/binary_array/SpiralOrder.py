#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/14 13:10
# @File    : SpiralOrder.py
from typing import List

"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        撞墙大法，使用方向遍历，[0, 1](向右),[1, 0](向下), [0, -1](向左), [-1, 0](向上)，依次遍历

        深度优先遍历
        :param matrix:
        :return:
        """
        paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row = len(matrix)
        col = len(matrix[0])

        result = []
        bad = False
        x, y = 0, -1
        cur_path = 0
        for i in range(row * col):
            # 根据当前的方向计算下一个位置
            nx, ny = x + paths[cur_path][0], y + paths[cur_path][1]
            # 撞到了墙
            if not 0 <= nx < row or not 0 <= ny < col or matrix[nx][ny] == bad:
                # 方向顺时针旋转90度
                cur_path = (cur_path + 1) % 4
                # 重新计算下一个位置
                nx, ny = x + paths[cur_path][0], y + paths[cur_path][1]

            result.append(matrix[nx][ny])
            # 标记遍历过的位置
            matrix[nx][ny] = bad
            x, y = nx, ny

        return result


if __name__ == '__main__':
    print(Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
