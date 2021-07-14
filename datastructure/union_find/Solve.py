#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/18 6:14
# @File    : Solve.py
from typing import List

"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}

    def find(self, x):
        """
        找到最终父结点，路径压缩方式
        :param x:
        :return:
        """
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def add(self, x):
        """
        往并查集中添加元素
        :param x:
        :return:
        """
        if x not in self.father:
            self.father[x] = x

    def merge(self, x, y):
        """
        合并并查集
        :param x:
        :param y:
        :return:
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        """
        检查并查集是否连通
        :param x:
        :param y:
        :return:
        """
        return x in self.father and y in self.father and self.find(x) == self.find(y)


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 并查集写法, 将所有在边界的'O'连接一个虚拟节点，其他连接自身所在位置
        if not board:
            return

        row = len(board)
        col = len(board[0])

        dummy = row * col
        union = UnionFind()
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union.add(i * col + j)
                        union.add(dummy)
                        union.merge(i * col + j, dummy)
                    else:
                        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            if board[i + x][j + y] == 'O':
                                union.add(i * col + j)
                                union.add((i + x) * col + j + y)
                                union.merge(i * col + j, (i + x) * col + j + y)

        # 处理数据
        for i in range(row):
            for j in range(col):
                if (i * col + j) in union.father and union.find(dummy) == union.find(i * col + j):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def solve1(self, board: List[List[str]]) -> None:
        """
        dfs方式
        :param self:
        :param board:
        :return:
        """
        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = '*'

            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                tmp_x = x + i
                tmp_y = y + j
                if 1 <= tmp_x < row and 1 <= tmp_y < col and board[tmp_x][tmp_y] == 'O':
                    dfs(tmp_x, tmp_y)

        # 遍历第一行和最后一行
        for i in range(col):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[row - 1][i] == 'O':
                dfs(row - 1, i)

        # 遍历第一列和最后一列
        for j in range(row):
            if board[j][0] == 'O':
                dfs(j, 0)
            if board[j][col - 1] == 'O':
                dfs(j, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'


if __name__ == '__main__':
    print(Solution().solve1([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]))
