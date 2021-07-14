#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 21:33
# @File    : SplitArray.py
from typing import List


class SplitArray(object):

    def __init__(self):
        pass

    def splitArray(self, nums: List[int], m: int) -> int:
        """
        使用二分查找，查找范围是[0, sum(nums)]
        :param nums:
        :param m:
        :return:
        """

        def get_split_number(mid):
            split_count = 1
            s = 0
            for i in nums:
                if s + i > mid:
                    s = i
                    split_count += 1
                else:
                    s += i
            return split_count > m

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (right - left) // 2 + left
            if get_split_number(mid):
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    pass
