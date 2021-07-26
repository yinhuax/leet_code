#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/18 11:14
# @File    : IntervalSum.py


class IntervalSum(object):

    def __init__(self):
        pass

    def binary_search(self, x, alls):
        """
        返回输入坐标的离散化下标
        :param x: 查询下标
        :param alls: 存储所有下标的数组
        :return:
        """
        left, right = 0, len(alls)

        while left < right:
            mid = (left + right) >> 1
            if alls[mid] >= x:
                right = mid
            else:
                left = mid + 1

        # 返回左区间位置
        return left

    def interval_sum(self, insert_arr, query_arr):
        """
        区间和模板，使用离散化操作减少查询时间复杂度
        :param insert_arr:  插入数组，包含2个数字，x, c  x表示插入的位置， c表示插入的数字
        :param query_arr:  轮询数组，包含2个数字，l， r  查询区间[l, r]之间所有数字的和
        :return:
        """
        alls = []
        for x, c in insert_arr:
            alls.append(x)

        for l, r in query_arr:
            alls.append(l)
            alls.append(r)

        # 对存储所有下标的数组进行排序去重复
        alls = list(sorted(set(alls)))
        a = [0] * len(alls)
        s = [0] * (len(alls) + 1)

        # 1. 存储插入数据
        for x, c in insert_arr:
            index = self.binary_search(x, alls)
            a[index] += c

        # 2. 计算前缀和
        for i in range(1, len(s)):
            s[i] = a[i - 1] + s[i - 1]

        # 查询
        for l, r in query_arr:
            l_index = self.binary_search(l, alls)
            r_index = self.binary_search(r, alls)
            print(s[r_index + 1] - s[l_index])


if __name__ == '__main__':
    insert_arr = [[1, 2], [3, 6], [7, 5]]
    query_arr = [[1, 3], [4, 6], [7, 8]]
    print(IntervalSum().interval_sum(insert_arr, query_arr))
