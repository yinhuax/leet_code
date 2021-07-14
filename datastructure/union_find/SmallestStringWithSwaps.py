#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/22 7:05
# @File    : SmallestStringWithSwaps.py
from typing import List

"""
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def find(self, x):
        """
        路径压缩
        :param x:
        :return:
        """
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        交互字符串中的元素
        :param s:
        :param pairs:
        :return:
        """
        from collections import defaultdict
        # 构建连通图
        uf = UnionFind()
        for i in range(len(s)):
            uf.add(i)

        # 合并交换索引
        for pair in pairs:
            uf.union(pair[0], pair[1])

        # 获取所有连通图
        connected_dict = defaultdict(list)
        for node in range(len(s)):
            connected_dict[uf.find(node)].append(node)

        res = list(s)
        # 重新赋值
        for nodes in connected_dict.values():
            indices = nodes
            string = sorted(res[node] for node in nodes)
            for i, ch in zip(indices, string):
                res[i] = ch

        return "".join(res)


if __name__ == '__main__':
    print(Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
