#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/7/30 18:32
# @File    : SubarraySum.py
from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        前缀和，数组长度20000
        :param nums:
        :param k:
        :return:
        """
        sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sums[i + 1] = nums[i] + sums[i]

        res = 0
        for i in range(1, len(nums) + 1):
            for j in range(i):
                if (sums[i] - sums[j]) == k:
                    res += 1

        return res

    def subarraySum1(self, nums: List[int], k: int) -> int:
        """
        使用字典优化前缀和
        :param nums:
        :param k:
        :return:
        """
        pre_sum_freq = dict()
        pre_sum_freq[0] = 1

        pre_sum = 0
        count = 0
        for num in nums:
            pre_sum += num

            count += pre_sum_freq.get(pre_sum - k, 0)
            pre_sum_freq[pre_sum] = pre_sum_freq.get(pre_sum, 0) + 1

        return count


if __name__ == '__main__':
    print(Solution().subarraySum1(nums=[1, 2, 3], k=3))
