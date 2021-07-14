#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/17 15:51
# @File    : LongestConsecutive.py
from typing import List

"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

 

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class UnionFind(object):

    def __init__(self):
        self.father = {}

    def find(self, x):
        if self.father[x] == x:
            return x

        # 压缩路径
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return (x in self.father) and (y in self.father) and (self.find(x) == self.find(y))

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def add(self, x):
        if x not in self.father:
            self.father[x] = x


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        并查集
        :param nums:
        :return:
        """
        # 首次遍历，添加数组元素并与邻居结盟
        nums_set = set(nums)

        union_find = UnionFind()
        for i in nums_set:
            union_find.add(i)
            union_find.add(i + 1)
            union_find.merge(i, i + 1)

        max_length = 0
        for i in nums_set:
            max_length = max(max_length, union_find.find(i) - i)
        return max_length


if __name__ == '__main__':
    print(Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
