#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/16 20:11
# @File    : PivotIndex.py
from typing import List

"""
给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/yf47s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class PivotIndex(object):

    def __init__(self):
        pass

    def pivotIndex(self, nums: List[int]) -> int:
        """
        使用数组前缀和，从左往右，返回第一次符合条件的索引，即可, 空间复杂度0, 时间复杂度0(N)
        :param nums:
        :return:
        """
        # 原地操作，计算数组前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        # 遍历数组，判断左右和右边和是否相等, 首尾不需要遍历
        left_sum = 0
        for i in range(0, len(nums)):
            if left_sum == (nums[len(nums) - 1] - nums[i]):
                return i
            left_sum = nums[i]

        return -1


if __name__ == '__main__':
    print(PivotIndex().pivotIndex([1, 7, 3, 6, 5, 6]))
