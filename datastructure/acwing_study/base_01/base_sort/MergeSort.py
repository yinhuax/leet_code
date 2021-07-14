#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/5 7:28
# @File    : MergeSort.py

"""
归并排序实现
"""


class MergeSort(object):

    def __init__(self):
        pass

    def merge_sort(self, arr, l, r):
        if l >= r:
            return

        # 先左边，后右边
        mid = (l + r) >> 1
        self.merge_sort(arr, l, mid)
        self.merge_sort(arr, mid + 1, r)
        self.merge(arr, l, r, mid)

    def merge(self, arr, l, r, mid):
        # 使用额外空间
        # 判断左边区间 和 右边区间哪个更小，就插入哪个
        i = l
        j = mid + 1
        tmp = []
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1

        tmp.extend(arr[i: mid + 1])
        tmp.extend(arr[j: r + 1])
        arr[l: r + 1] = tmp


if __name__ == '__main__':
    arr = [1, 3, 2, 5, 4, 6]
    MergeSort().merge_sort(arr, 0, len(arr) - 1)
    print(arr)
