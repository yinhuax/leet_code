#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/12 12:47
# @File    : PrefixSum.py

"""
前缀和模板
"""


class PrefixSum(object):

    def __init__(self):
        pass

    def prefix_sum(self, arr, l, r):
        """
        前缀和，输入一个数组，[l, r]，输出从l 到 r的和
        :param arr:
        :param l:
        :param r:
        :return:
        """
        # 预留边界，减少判断
        sums = [0] * (len(arr) + 1)
        # 初始化前缀和数组， 使得S[i] = S[i - 1] + arr[i - 1]
        for i in range(1, len(sums)):
            sums[i] = sums[i - 1] + arr[i - 1]

        # 区间和为S[r] - S[l - 1]，这里S第一个位置填充了0，所以全部+1移动一位
        return sums[r + 1] - sums[l]


if __name__ == '__main__':
    print(PrefixSum().prefix_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5))
