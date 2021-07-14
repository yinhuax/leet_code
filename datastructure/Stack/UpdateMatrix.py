#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/14 21:36
# @File    : UpdateMatrix.py
from typing import List


class UpdateMatrix(object):

    def __init__(self):
        pass

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        广度优先遍历，加
        :param matrix:
        :return:
        """
        from collections import deque
        row = len(matrix)
        col = len(matrix[0])

        # 使用队列，广搜
        def bfs(cur_x, cur_y):
            queue = deque()
            queue.append((cur_x, cur_y))

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for r, c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        tmp_x = x + r
                        tmp_y = y + c
                        if 0 <= tmp_x < row and 0 <= tmp_y < col:
                            if matrix[tmp_x][tmp_y] != 0:
                                queue.append((tmp_x, tmp_y))
                            elif matrix[tmp_x][tmp_y] == 0:
                                matrix[cur_x][cur_y] = abs(cur_x - tmp_x) + abs(cur_y - tmp_y)
                                return

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    bfs(i, j)

        return matrix

    def updateMatrix1(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10 ** 9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist

if __name__ == '__main__':
    matrix = [[0, 1, 0],
              [0, 1, 0],
              [0, 1, 0],
              [0, 1, 0],
              [0, 1, 0]]
    print(UpdateMatrix().updateMatrix(matrix))
