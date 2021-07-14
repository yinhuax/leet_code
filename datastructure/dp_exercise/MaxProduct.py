#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/13 7:51
# @File    : MaxProduct.py
from typing import List

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return

        res = nums[0]
        max_res = nums[0]
        min_res = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(min_res * nums[i], nums[i], max_res * nums[i])
            cur_min = min(min_res * nums[i], nums[i], max_res * nums[i])
            res = max(res, cur_max)
            max_res = cur_max
            min_res = cur_min

        return res


if __name__ == '__main__':
    print(Solution().maxProduct([-4, -3, -2]))
