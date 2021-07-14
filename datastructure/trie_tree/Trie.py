#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 11:09
# @File    : Trie.py
"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
"""
from collections import defaultdict

"""
前缀树实现
"""


class TrieNode(object):

    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for s in word:
            node = node.children[s]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for s in word:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return True
