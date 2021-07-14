#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/14 9:44
# @File    : CanJump.py
from typing import List

"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
"""


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            """
            判断前一个能达到的最远位置是否大于当前位置
            """
            if dp[i - 1] < i:
                return False
            else:
                dp[i] = max(dp[i - 1], i + nums[i])
                if dp[i] >= len(nums) - 1:
                    return True

        return False

    def canJump1(self, nums: List[int]) -> bool:
        """
        注意到 下标i只与下标i - 1有关，优化空间为O(1)
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False

        max_jump = nums[0]
        for i in range(1, len(nums)):
            if max_jump < i:
                return False
            else:
                max_jump = max(max_jump, i + nums[i])
                if max_jump >= len(nums) - 1:
                    return True

        return False