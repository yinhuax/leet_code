#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/26 15:02
# @File    : MaxSubArray.py
from typing import List

"""
最大子序和
"""


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子序和，动态规划
        :param nums:
        :return:
        """
        max_res = nums[0]
        pre = 0
        for num in nums:
            # 如果有增益就加上
            pre = max(pre + num, num)
            max_res = max(max_res, pre)

        return max_res


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
