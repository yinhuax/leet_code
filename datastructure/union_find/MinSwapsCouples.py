#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/20 7:42
# @File    : MinSwapsCouples.py
from typing import List

"""
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

示例 1:

输入: row = [0, 2, 1, 3]
输出: 1
解释: 我们只需要交换row[1]和row[2]的位置即可。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/couples-holding-hands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, x):
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
            self.father[root_x] = self.father[root_y]
            self.count -= 1

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)


class Solution:

    def minSwapsCouples(self, row: List[int]) -> int:
        """
        并查集
        :param row:
        :return:
        """
        uf = UnionFind()
        for i in range(len(row)):
            uf.add(row[i] // 2)

        for i in range(0, len(row), 2):
            uf.merge(row[i] // 2, row[i + 1] // 2)

        return len(row) // 2 - uf.count


if __name__ == '__main__':
    print(Solution().minSwapsCouples(row=[0, 2, 1, 3]))
