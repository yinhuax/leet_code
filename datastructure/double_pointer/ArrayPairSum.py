#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/25 23:31
# @File    : ArrayPairSum.py
from typing import List


class ArrayPairSum(object):

    def __init__(self):
        pass

    def arrayPairSum(self, nums: List[int]) -> int:
        """
        排序数组，将值接近的放到一起
        :param nums:
        :return:
        """
        nums.sort()
        sums = 0
        for i in range(0, len(nums), 2):
            sums += nums[i]
        return sums


if __name__ == '__main__':
    print(ArrayPairSum().arrayPairSum([1, 4, 3, 2]))
