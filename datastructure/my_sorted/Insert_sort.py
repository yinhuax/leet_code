#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 15:03
# @File    : Insert_sort.py


class Insert_sort(object):

    def insert_sort(self, alist):
        n = len(alist)
        for i in range(1, n):
            while i > 0:
                if alist[i] < alist[i - 1]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                else:
                    break

        return alist


if __name__ == '__main__':
    print(Insert_sort().insert_sort([1, 3, 6, 4, 5, 7, 9]))
