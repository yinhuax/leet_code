#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 15:29
# @File    : Intersection2.py
from typing import List

"""
给定两个数组，编写一个函数来计算它们的交集。两个数组交集二
"""


class Intersection2(object):

    def __init__(self):
        pass

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        哈希表做法，时间复杂度O(M+N), 空间复杂度O(max(M, N))
        :param nums1:
        :param nums2:
        :return:
        """
        seen = dict()

        for i in nums1:
            seen.setdefault(i, 0)
            seen[i] += 1

        intersect = []
        for j in nums2:
            if seen.get(j, 0) != 0:
                seen[j] -= 1
                intersect.append(j)
                if seen.get(j) == 0:
                    seen.pop(j)

        return intersect

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        排序加双指针做法
        :param nums1:
        :param nums2:
        :return:
        """
        nums1.sort()
        nums2.sort()

        l1 = 0
        l2 = 0
        intersect = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] < nums2[l2]:
                l1 += 1
            elif nums1[l1] == nums2[l2]:
                intersect.append(nums1[l1])
                l1 += 1
                l2 += 1
            else:
                l2 += 1
        return intersect
