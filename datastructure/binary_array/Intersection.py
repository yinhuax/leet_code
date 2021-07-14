#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 15:10
# @File    : Intersection.py
from typing import List

"""
给定两个数组，编写一个函数来计算它们的交集。
"""


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        求交集
        :param nums1:
        :param nums2:
        :return:
        """
        # 哈希表
        return list(set(nums1) & set(nums2))
