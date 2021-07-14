#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/5 18:05
# @File    : BinarySearch.py


class BinarySearch(object):

    def check(self, arr, mid, target):
        return arr[mid] == target

    def bsearch_l(self, arr, l, r, target):
        # 定位左边界，区间[l, mid] 被划分为[l, mid] 和 [mid + 1, r]时使用
        while l < r:
            mid = l + r >> 1
            if self.check(arr, mid, target):
                r = mid
            else:
                l = mid + 1
        return l

    def bsearch_r(self, arr, l, r, target):
        # 定位右边界，区间[l, r] 被划分为[l, mid - 1] 和 [mid, r]时使用
        while l < r:
            mid = (l + r + 1) >> 1
            if self.check(arr, mid, target):
                l = mid
            else:
                r = mid - 1
        return l

    def bsearch_float(self, r):
        """
        浮点型 二分
        :param arr:
        :param target:
        :return:
        """
        x = r
        l = 0
        while (r - l) > 1e-6:
            mid = (l + r) / 2
            if (mid * mid) >= x:
                r = mid
            else:
                l = mid
        return round(l, 4)


if __name__ == '__main__':
    # 测试
    arr = [1, 2, 3, 3, 4, 5]
    target = 3
    # print(BinarySearch().bsearch_r(arr, 0, len(arr) - 1, target))
    print(BinarySearch().bsearch_float(100))
