#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/22 7:30
# @File    : EquationsPossible.py
from typing import List

"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = x

    def find(self, x):
        if x == self.father[x]:
            return x

        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        """
        等式方程的可满足性
        :param equations:
        :return:
        """
        uf = UnionFind()

        for equation in equations:
            s1 = equation[0]
            s2 = equation[-1]
            uf.add(s1)
            uf.add(s2)

        for equation in equations:
            if equation[1] == '=':
                # 构建连通图
                s1 = equation[0]
                s2 = equation[-1]
                uf.union(s1, s2)

        # 查看连通图是否冲突
        for equation in equations:
            if equation[1] == '!':
                s1 = equation[0]
                s2 = equation[-1]
                if uf.is_connected(s1, s2):
                    return False

        return True


if __name__ == '__main__':
    print(Solution().equationsPossible(["b!=a"]))
