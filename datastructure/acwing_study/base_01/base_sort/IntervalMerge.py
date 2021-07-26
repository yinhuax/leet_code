#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/18 12:35
# @File    : IntervalMerge.py


class IntervalMerge(object):

    def __init__(self):
        pass

    def interval_merge(self, arr):
        """
        区间合并
        :param arr:
        :return:
        """
        # 先对数组进行排序
        arr = sorted(arr)
        start = -10 ** 9
        end = -10 ** 9
        result = []
        for l, r in arr:
            # 如果 l 大于end，直接将 start, end 保存到数组
            if l > end:
                if end != -10 ** 9:
                    result.append([start, end])
                start = l
                end = r
            # 如果 start < l < end，end = max(end, r)
            else:
                end = max(end, r)

        if start != -10 ** 9:
            result.append([start, end])

        print(result)


if __name__ == '__main__':
    print(IntervalMerge().interval_merge([[1, 2], [2, 4], [5, 6], [7, 9], [10, 11]]))
