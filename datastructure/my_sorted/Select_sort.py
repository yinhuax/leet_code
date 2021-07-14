#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 12:03
# @File    : Select_sort.py


class Select_sort(object):

    def select_sort(self, alist):
        n = len(alist)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if alist[j] < alist[min_index]:
                    min_index = j

            alist[min_index], alist[i] = alist[i], alist[min_index]

        return alist


if __name__ == '__main__':
    print(Select_sort().select_sort([1, 2, 6, 5, 7, 0, 9]))
