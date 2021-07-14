#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 11:35
# @File    : SearchRange.py
from typing import List


class SearchRange(object):

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        范围搜索
        :param nums:
        :param target:
        :return:
        """
        # 查找目标值左边界
        if not nums:
            return [-1, -1]
        left = self.binary_search_l(nums, target)
        if left == -1:
            return [-1, -1]
        # 查找目标值右边界
        right = self.binary_search_r(nums, target)
        return [left, right]

    def binary_search_l(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left if nums[left] == target else - 1

    def binary_search_r(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left + 1) // 2 + left
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(SearchRange().searchRange([5, 7, 7, 8, 8, 10], 8))
