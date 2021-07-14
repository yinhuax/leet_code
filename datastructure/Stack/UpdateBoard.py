#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/24 8:40
# @File    : UpdateBoard.py
from typing import List

"""
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，
'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minesweeper
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        dfs
        :param board:
        :param click:
        :return:
        """
        n = len(board)
        m = len(board[0])

        # 第一步点击到了地雷
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        paths = ((1, 1), (1, -1), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1))

        def dfs(i, j):
            # 统计相邻的地雷数量
            num = 0
            for x, y in paths:
                tem_i = i + x
                tem_j = j + y
                if 0 <= tem_i < n and 0 <= tem_j < m and board[tem_i][tem_j] == 'M':
                    num += 1

            if num > 0:
                board[i][j] = str(num)
            else:
                board[i][j] = 'B'
                for x, y in paths:
                    tem_i = i + x
                    tem_j = j + y
                    if 0 <= tem_i < n and 0 <= tem_j < m and board[tem_i][tem_j] == 'E':
                        dfs(tem_i, tem_j)

        dfs(click[0], click[1])
        return board


if __name__ == '__main__':
    print(Solution().updateBoard([['E', 'E', 'E', 'E', 'E'],
                                  ['E', 'E', 'M', 'E', 'E'],
                                  ['E', 'E', 'E', 'E', 'E'],
                                  ['E', 'E', 'E', 'E', 'E']], [3, 0]))
