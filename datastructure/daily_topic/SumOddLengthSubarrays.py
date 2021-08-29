#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/30 6:14
# @File    : SumOddLengthSubarrays.py
from typing import List

"""
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        前缀和
        :param arr:
        :return:
        """
        sums = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            sums[i + 1] = sums[i] + arr[i]

        all_sums = 0
        for i in range(1, len(arr) + 1):
            for j in range(i, len(arr) + 1):
                if (j - i + 1) % 2 == 1:
                    all_sums += sums[j] - sums[i - 1]

        return all_sums


if __name__ == '__main__':
    print(Solution().sumOddLengthSubarrays([1]))
