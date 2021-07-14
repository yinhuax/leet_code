#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 10:41
# @File    : Bubble_sort.py


class Bubble_sort(object):

    def bubble_sort(self, alist):
        """
        冒泡排序
        :param alist:
        :return:
        """
        n = len(alist)
        # 原理，每次选出一个最大值，排在最后一个
        for i in range(n - 1, 0, -1):
            count = 0
            for j in range(i):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
                    count += 1
            if 0 == count:
                break

        return alist


if __name__ == '__main__':
    print(Bubble_sort().bubble_sort([1, 3, 4, 6, 7, 5, 9]))
