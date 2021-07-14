#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 21:10
# @File    : SmallestDistancePair.py
from typing import List

"""
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
"""


class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        排序+二分，最大差值为max - min，最小差值为0，使用二分查找符合条件的查找，边界定义为符合当前差值条件的k个对
        :param nums:
        :param k:
        :return:
        """
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (right - left) // 2 + left
            cnt, start = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start

            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left
