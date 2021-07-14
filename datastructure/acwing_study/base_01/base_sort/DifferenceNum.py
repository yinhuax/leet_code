#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/12 20:11
# @File    : DifferenceNum.py

"""
差分数组
"""


class DifferenceNum(object):

    def __init__(self):
        pass

    def insert(self, b_arr, l, r, c):
        b_arr[l] += c
        b_arr[r + 1] -= c

    def diff_num(self, arr, add_arr):
        """
        前缀和逆运算， 快速给区间 加上指定值
        :param arr:
        :param l:
        :param r:
        :param c:
        :return:
        """
        # 防止下标越界，多初始化2个下标
        b_arr = [0] * (len(arr) + 2)
        for i in range(1, len(arr) + 1):
            self.insert(b_arr, i, i, arr[i - 1])

        # 插入l, r, c
        for l, r, c in add_arr:
            self.insert(b_arr, l, r, c)

        for i in range(1, len(arr) + 1):
            b_arr[i] += b_arr[i - 1]

        return b_arr[1: len(arr) + 1]


if __name__ == '__main__':
    print(DifferenceNum().diff_num([1, 2, 2, 1, 2, 1], [[1, 3, 1], [3, 5, 1], [1, 6, 1]]))
