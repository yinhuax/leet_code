#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/12 14:44
# @File    : WordDictionary.py
from collections import defaultdict

"""
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/trie/x0jtri/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TrieTree(object):

    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieTree)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieTree()

    def addWord(self, word: str) -> None:
        node = self.root
        for s in word:
            node = node.children[s]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        搜索，支持模糊匹配
        :param word:
        :return:
        """
        self.res = False

        def bfs_search(i, node):
            if node.is_word and i == len(word):
                self.res = True
                return

            if i >= len(word):
                return False

            if word[i] == '.':
                # 搜索当前层所有节点
                for children in node.children:
                    # 不能在外面复制，指针引用会改变当前递归的结果
                    bfs_search(i + 1, node.children[children])
            elif word[i] in node.children:
                bfs_search(i + 1, node.children[word[i]])
            else:
                return

        bfs_search(0, self.root)
        return self.res


if __name__ == '__main__':
    word_dictionary = WordDictionary()
    word_dictionary.addWord('at')
    word_dictionary.addWord('and')
    word_dictionary.addWord('an')
    word_dictionary.addWord('add')
    print(word_dictionary.search('a'))
    print(word_dictionary.search('.at'))
    word_dictionary.addWord('bat')
    print(word_dictionary.search('.at'))
    print(word_dictionary.search('an.'))
    print(word_dictionary.search('a.d.'))
    print(word_dictionary.search('b.'))
    print(word_dictionary.search('a.d'))
    print(word_dictionary.search('.'))
