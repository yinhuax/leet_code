#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/3 23:39
# @File    : IsValidSudoku.py
from typing import List


class IsValidSudoku(object):

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        使用三个哈希表存储行、列、单独格子中出现过的数字，如果再次出现返回false
        :param board:
        :return:
        """
        from collections import defaultdict
        hash_table_r = defaultdict(set)
        hash_table_l = defaultdict(set)
        hash_table = defaultdict(set)

        # 行
        for i in range(len(board)):
            # 列
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    hash_table_r.setdefault(i, set())
                    if board[i][j] in hash_table_r[i]:
                        return False
                    else:
                        hash_table_r[i].add(board[i][j])

                    hash_table_l.setdefault(j, set())
                    if board[i][j] in hash_table_l[j]:
                        return False
                    else:
                        hash_table_l[j].add(board[i][j])

                    cur_index = (i // 3) * 3 + j // 3
                    hash_table.setdefault(cur_index, set())
                    if board[i][j] in hash_table[cur_index]:
                        return False
                    else:
                        hash_table[cur_index].add(board[i][j])

        return True
