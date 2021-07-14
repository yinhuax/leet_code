#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/13 19:50
# @File    : WordSearch.py
from typing import List

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        回溯算法
        :param board:
        :param word:
        :return:
        """
        row = len(board)
        col = len(board[0])

        n = len(word)

        def dfs(x, y, s):
            if len(s) == n and s == word:
                return True

            if len(s) >= n:
                return False

            tmp_s = board[x][y]
            board[x][y] = False
            for tmp_i, tmp_j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_i = x + tmp_i
                next_j = y + tmp_j

                if 0 <= next_i < row and 0 <= next_j < col and board[next_i][next_j]:
                    next_s = s + board[next_i][next_j]
                    if next_s == word[: len(next_s)]:
                        if dfs(next_i, next_j, next_s):
                            return True
            board[x][y] = tmp_s

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[0]):
                        return True

        return False


if __name__ == '__main__':
    print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
