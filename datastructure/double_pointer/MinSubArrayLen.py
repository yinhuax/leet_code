#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/28 23:56
# @File    : MinSubArrayLen.py
from typing import List

"""
长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c0w4r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class MinSubArrayLen(object):

    def __init__(self):
        pass

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        双指针，或者二分查找写法(前缀和)
        :param s:
        :param nums:
        :return:
        """

        sums = 0
        start = 0
        min_len = len(nums) + 1
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                min_len = min(min_len, i - start + 1)
                sums -= nums[start]
                start += 1

        return 0 if min_len == len(nums) + 1 else min_len

    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        """
        双指针，或者二分查找写法(前缀和)
        :param s:
        :param nums:
        :return:
        """
        # 二分查找写法，使用前缀和
        # 原地修改原始数组
        if not nums:
            return 0

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        if nums[-1] < s:
            return 0
        if nums[-1] == s:
            return len(nums)

        min_len = len(nums)
        for i in range(len(nums)):
            if nums[i] < s:
                continue

            cur_diff = nums[i] - s
            left = self.binary_search(cur_diff, nums)
            if nums[left] + s <= nums[i]:
                min_len = min(min_len, i - left)
            else:
                min_len = min(min_len, i - left + 1)

        return min_len

    def binary_search(self, target, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left + 1) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(MinSubArrayLen().minSubArrayLen1(s=5, nums=[2, 3, 1, 1, 1, 1, 1]))
