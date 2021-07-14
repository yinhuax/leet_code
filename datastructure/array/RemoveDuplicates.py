#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/8 8:14
# @File    : RemoveDuplicates.py
from typing import List

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x9a60t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        使用双指针
        :param nums:
        :return:
        """
        left = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[left]:
                left += 1
                nums[i], nums[left] = nums[left], nums[i]

        return left + 1
