#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 14:33
# @File    : Intersection.py
from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        计算交集
        :param nums1:
        :param nums2:
        :return:
        """
        return list(set(nums1) & set(nums2))
