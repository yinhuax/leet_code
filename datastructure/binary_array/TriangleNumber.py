#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/29 18:39
# @File    : TriangleNumber.py
from typing import List

"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
"""


class Solution:

    def triangleNumber(self, nums: List[int]) -> int:
        """
        先排序， 根据 三角形的定理， 只要排序后 a + b > c, a < b < c，就可以构成三角形
        :param nums:
        :return:
        """
        nums.sort()

        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                sums = nums[i] + nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    mid = (left + right + 1) >> 1
                    if sums > nums[mid]:
                        left = mid
                    else:
                        right = mid - 1

                if nums[right] < sums:
                    res += right - j

        return res


if __name__ == '__main__':
    print(Solution().triangleNumber([2, 2, 3, 4]))
