#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/9/1 17:45
# @File    : SortArray.py
from typing import List

"""
给你一个整数数组 nums，请你将该数组升序排列。
"""


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        堆排
        :param nums:
        :return:
        """
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.builde_head(i, n - 1, nums)

        # 调整大顶堆
        for j in range(n - 1, -1, -1):
            nums[j], nums[0] = nums[0], nums[j]
            self.builde_head(0, j - 1, nums)

        return nums

    # 构建大顶堆
    def builde_head(self, i, n, head):
        left, right = 2 * i + 1, 2 * i + 2

        max_index = i
        if left <= n and head[left] > head[max_index]:
            max_index = left

        if right <= n and head[right] > head[max_index]:
            max_index = right

        if max_index != i:
            head[max_index], head[i] = head[i], head[max_index]
            return self.builde_head(max_index, n, head)

    def sortArray1(self, nums: List[int]) -> List[int]:
        """
        归并排序
        :param nums:
        :return:
        """
        self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return

        mid = left + right >> 1
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, right, mid)

    def merge(self, arr: List[int], left, right, mid):
        """
        需要额外空间
        :param arr:
        :return:
        """
        i = left
        j = mid + 1

        temp = []
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        temp.extend(arr[i: mid + 1])
        temp.extend(arr[j: right + 1])

        arr[left:right + 1] = temp

    def sortArray2(self, nums: List[int]) -> List[int]:
        """
        快排实现
        :param nums:
        :return:
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, arr, left, right):
        if left >= right:
            return

        x = arr[right]

        i = left
        j = right
        while i < j:
            while i < j and arr[j] > x:
                j -= 1

            while i < j and arr[i] <= x:
                i += 1

            if i < j:
                # 交换数据
                arr[i], arr[j] = arr[j], arr[i]
                if arr[i] == arr[j] == x:
                    i += 1
                    j -= 1

        # arr[left], arr[j] = arr[j], arr[left]
        self.quick_sort(arr, left, j - 1)
        self.quick_sort(arr, j, right)
