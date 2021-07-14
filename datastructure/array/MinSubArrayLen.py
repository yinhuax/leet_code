#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 7:04
# @File    : MinSubArrayLen.py
from typing import List

"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x9gogt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        双指针，滑动窗口
        :param target:
        :param nums:
        :return:
        """
        sums = 0
        start = 0
        min_len = len(nums) + 1
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= target:
                min_len = min(min_len, i - start + 1)
                sums -= nums[start]
                start += 1
        return 0 if min_len == len(nums) + 1 else min_len

    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        """
        前缀和 + 二分查找
        :param target:
        :param nums:
        :return:
        """
        # 计算数组前缀和
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        if nums[-1] < target:
            return 0

        if nums[-1] == target:
            return len(nums)

        min_len = len(nums)
        for i in range(len(nums)):
            if nums[i] < target:
                continue

            cur_diff = nums[i] - target
            # 二分查找
            left = self.binary_search(cur_diff, nums)
            if nums[left] + target <= nums[i]:
                min_len = min(min_len, i - left)
            else:
                min_len = min(min_len, i - left + 1)

        return min_len

    def binary_search(self, target: int, nums: List[int]):
        left, right = 0, len(nums) - 1
        while left < right:
            # 查找左边界
            mid = (right - left + 1) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    print(Solution().minSubArrayLen1(7, [2, 3, 1, 2, 4, 3]))
