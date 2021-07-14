#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/16 20:33
# @File    : SearchInsert.py

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素
"""
from typing import List


class SearchInsert(object):

    def __init__(self):
        pass

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        使用二分查找最快时间复杂度log(n)
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1

        # if nums[-1] < target:
        #     return len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left


if __name__ == '__main__':
    print(SearchInsert().searchInsert([1, 3, 5, 6], 0))
