#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 7:39
# @File    : MaxSubArray.py
from typing import List

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

"""


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子序和，dp
        :param nums:
        :return:
        """
        pre = 0
        result = nums[0]
        for num in nums:
            pre = max(num, pre + num)
            result = max(pre, result)

        return result
