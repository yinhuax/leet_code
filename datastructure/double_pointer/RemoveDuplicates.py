#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 11:40
# @File    : RemoveDuplicates.py
from typing import List


class RemoveDuplicates(object):

    def __init__(self):
        pass

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        双指针，移除重复元素
        :param nums:
        :return:
        """
        first = 0
        for i in range(len(nums)):
            if nums[i] != nums[first]:
                first += 1
                nums[first] = nums[i]

        return first + 1


if __name__ == '__main__':
    print(RemoveDuplicates().removeDuplicates([1, 1, 2]))
