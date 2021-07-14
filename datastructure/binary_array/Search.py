#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 8:04
# @File    : Search.py
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """
        一次遍历查找
        :param nums:
        :param target:
        :return:
        """
        for i, j in enumerate(nums):
            if j == target:
                return i

        return -1

    def search1(self, nums: List[int], target: int):
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left if nums[left] == target else -1

    def search2(self, nums: List[int], target: int):
        """
        二分查找基本模板
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return -1




if __name__ == '__main__':
    print(Solution().search1(nums=[2, 5], target=5))
