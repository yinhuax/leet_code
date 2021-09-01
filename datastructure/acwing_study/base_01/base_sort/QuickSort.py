#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/4 20:58
# @File    : QuickSort.py


class QuickSort(object):

    def __init__(self):
        pass

    def quick_sort(self, q, l, r):
        if l >= r:
            return
        x = arr[r]
        i = l
        j = r
        while i < j:
            while i < j and arr[j] > x: j -= 1
            while i < j and arr[i] <= x: i += 1

            if i < j:
                # 交换位置
                arr[i], arr[j] = arr[j], arr[i]
                if arr[i] == arr[j] == x:
                    i += 1
                    j -= 1
        # self.quick_sort(arr, l, i - 1)
        # self.quick_sort(arr, i, r)

        self.quick_sort(arr, l, j - 1)
        self.quick_sort(arr, j, r)
        # if l >= r:
        #     return
        # x = q[(l + r) // 2]
        # i, j = l - 1, r + 1
        # while i < j:
        #     # python do while 写法，避免重复元素导致快排超时  i < j && q[i] == x && q[j] == x 死循环了
        #     while True:
        #         i += 1
        #         if q[i] >= x:
        #             break
        #     while True:
        #         j -= 1
        #         if q[j] <= x:
        #             break
        #     if i < j:
        #         q[i], q[j] = q[j], q[i]
        # self.quick_sort(q, l, j)
        # self.quick_sort(q, j + 1, r)


if __name__ == '__main__':
    arr = [-1, 2, -8, -10]
    QuickSort().quick_sort(arr, 0, len(arr) - 1)
    print(arr)
