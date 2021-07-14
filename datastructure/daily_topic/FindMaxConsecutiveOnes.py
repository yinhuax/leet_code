#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/15 8:51
# @File    : FindMaxConsecutiveOnes.py
from typing import List

"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:
"""


class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        动态规划
        :param nums:
        :return:
        """
        ans = 0 if nums[0] != 1 else 1
        max_len = ans
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] == 1:
                ans += 1
            elif nums[i]:
                ans = 1
            else:
                ans = 0
            max_len = max(max_len, ans)

        return max_len


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
