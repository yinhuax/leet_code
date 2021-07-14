#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/21 20:14
# @File    : NumSimilarGroups.py
from typing import List

"""
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。

总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。
形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/similar-string-groups
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, x):
        """
        路径压缩
        :param x:
        :return:
        """
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.count += 1

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)


class Solution:

    def numSimilarGroups(self, strs: List[str]) -> int:
        """
        使用并查集，将相似字符串构建为并查集，时间复杂度O(n ^ 2)
        :param strs:
        :return:
        """
        uf = UnionFind()
        for i in range(len(strs)):
            uf.add(strs[i])
            for j in range(i + 1, len(strs)):
                # 判断是否相似，如果相似构建并查集
                if self.is_similar(strs[i], strs[j]):
                    uf.add(strs[j])
                    uf.merge(strs[i], strs[j])

        return uf.count

    def is_similar(self, str1, str2):
        count = 0
        if len(str1) != len(str2):
            return False

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
            if count > 2:
                return False

        return True


if __name__ == '__main__':
    print(Solution().numSimilarGroups(["tars", "rats", "arts", "star"]))
