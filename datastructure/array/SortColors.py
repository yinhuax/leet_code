#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 9:01
# @File    : SortColors.py
from typing import List

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x9wv2h/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 计数排序法，常数空间，两遍扫描
        count1 = 0
        count2 = 0
        count3 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count1 += 1
            elif nums[i] == 1:
                count2 += 1
            else:
                count3 += 1

        for i in range(len(nums)):
            if i < count1:
                nums[i] = 0
            elif count1 <= i < count1 + count2:
                nums[i] = 1
            else:
                nums[i] = 2

    def sortColors1(self, nums: List[int]) -> None:
        """
        单指针排序
        :param nums:
        :return:
        """
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        for i in range(p, n):
            if nums[i] == 1:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

    def sortColors2(self, nums: List[int]) -> None:
        """
        双指针排序, 分别使用2个指针，p1、p2， p1存储0从0开始往后遍历, p2存储2，从len(nums) - 1开始往前遍历
        :param nums:
        :return:
        """
        n = len(nums)
        p1, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            i += 1


if __name__ == '__main__':
    print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
