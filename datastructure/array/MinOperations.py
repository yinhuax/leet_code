#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/27 16:27
# @File    : MinOperations.py
from typing import List

"""
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

 

示例 1：

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        """
        滑动窗口
        :param nums:
        :param x:
        :return:
        """
        sums = sum(nums)
        target = sums - x
        if target < 0:
            return -1

        left, right = 0, 0
        max_len = float('-inf')
        while right < len(nums):
            # 窗口向右扩展
            target -= nums[right]
            right += 1

            while target < 0:
                target += nums[left]
                left += 1

            if target == 0:
                max_len = max(max_len, right - left)

        return -1 if max_len == float('-inf') else len(nums) - max_len
