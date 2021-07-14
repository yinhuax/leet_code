#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 16:42
# @File    : FindWords.py
from typing import List

"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/trie/x7hd9g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from collections import defaultdict


class TrieTree(object):

    def __init__(self):
        self.children = defaultdict(TrieTree)
        self.is_word = ''


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        使用前缀树+深度优先搜索
        :param board:
        :param words:
        :return:
        """
        root = TrieTree()
        n = len(board)
        m = len(board[0])

        for word in words:
            cur_node = root
            for s in word:
                cur_node = cur_node.children[s]
            cur_node.is_word = word

        def dfs(i, j, node):
            latter = board[i][j]
            if latter not in node.children:
                return

            if node.children[latter].is_word:
                result.append(node.children[latter].is_word)
                # 这个单词已经找到过了
                node.children[latter].is_word = ''

            # 标记防止重复
            board[i][j] = '#'
            for tem_i, tem_j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                index_i = tem_i + i
                index_j = tem_j + j
                if 0 <= index_i < n and 0 <= index_j < m and board[index_i][index_j] in node.children[latter].children:
                    dfs(index_i, index_j, node.children[latter])

            board[i][j] = latter

        result = []
        for i in range(n):
            for j in range(m):
                dfs(i, j, root)

        return result


if __name__ == '__main__':
    print(Solution().findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]))
