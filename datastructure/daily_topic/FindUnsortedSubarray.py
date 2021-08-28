#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/3 7:10
# @File    : FindUnsortedSubarray.py
from typing import List

"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        排序对比
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return 0

        def isSorted(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        if isSorted(nums):
            return 0

        new_nums = sorted(nums)
        left = 0
        while nums[left] == new_nums[left]:
            left += 1

        right = len(new_nums) - 1
        while nums[right] == new_nums[right]:
            right -= 1

        return right - left + 1

    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        """
        1. 从左往右遍历，找到后面更小的值，不满足升序，当前值应该被排序
        2. 从右往左遍历，找到前面更大的值，不满足升序，当前值应该被排序
        :param nums:
        :return:
        """
        if len(nums) <= 0:
            return 0

        r = 0
        min_v = nums[0]
        for i in range(len(nums)):
            if nums[i] < min_v:
                r = i
            else:
                min_v = nums[i]

        l = len(nums) - 1
        max_v = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_v:
                l = i
            else:
                max_v = nums[i]

        return max(r - l + 1, 0)


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray1([1]))
