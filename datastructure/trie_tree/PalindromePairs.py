#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 18:28
# @File    : PalindromePairs.py
from typing import List

"""
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
"""

from collections import defaultdict


class TireTree(object):

    def __init__(self):
        # 用于记录下标
        self.is_word = -1
        self.children = defaultdict(TireTree)


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        前缀树，使用逆序方式构建前缀树
        判断两个单词是否能构成回文串的方式，
        s1 代表当前遍历字符串，s2 代表在前缀树中遍历得到的字符串
        1. 长度相同，s1 == s2
        2. 长度不同，len(s1) > len(s2)，s2 先遍历到头，返回index，识别s1[:len(s1) - len(s2)]是否回文
        2. 长度不同，len(s1) < len(s2)，s1 先遍历到头，s2 继续遍历，识别s2[:len(s2) - len(s1)]是否回文
        :param words:
        :return:
        """
        # 构建前缀树
        root = TireTree()
        for index, word in enumerate(words):
            cur_node = root
            for i in range(len(word)):
                cur_node = cur_node.children[word[i]]
            cur_node.is_word = index

        # 遍历数组查找，满足回文数条件的字符串
        result = []
        for index, word in enumerate(words):
            cur_node = root
            left = len(word)
            right = 0
            for i in range(len(word) - 1, -1, -1):
                # 从前缀树中找到指定前缀
                if word[i] in cur_node.children and cur_node.is_word == -1:
                    cur_node = cur_node.children[word[i]]
                    right += 1
                elif word[i] not in cur_node.children and cur_node.is_word == -1:
                    # 不符合条件
                    break
                elif word[i] not in cur_node.children and cur_node.is_word != -1:
                    # s2 更短，判断剩下的字符串是否为回文串
                    if word[i - 1: left - i] == word[i - 1: left - i][::-1] and index != cur_node.is_word:
                        result.append([index, cur_node.is_word])
                        break

            if cur_node.is_word != -1 and index != cur_node.is_word:
                # len(s1) == len(s2)
                result.append([index, cur_node.is_word])

            if right == left and cur_node.is_word == -1:
                # s1 更短
                # 判断后缀是否回文
                self.suffix = []
                self.dfs_search(cur_node, '')
                # 判断是否回文
                for x in self.suffix:
                    if x[1] == x[1][::-1] and x[0] != index:
                        result.append([index, x[0]])

        return result

    def dfs_search(self, root, s):
        if root.is_word != -1:
            self.suffix.append([root.is_word, s])
            return

        for children in root.children:
            return self.dfs_search(root.children[children], s + children)


if __name__ == '__main__':
    print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
