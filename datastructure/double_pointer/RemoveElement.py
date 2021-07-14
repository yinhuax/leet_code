#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/28 23:27
# @File    : RemoveElement.py
from typing import List


class RemoveElement(object):

    def __init__(self):
        pass

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        使用双指针，空间复杂度O(1)，时间复杂度O(n)
        :param nums:
        :param val:
        :return:
        """
        drop_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[drop_index] = nums[i]
                drop_index += 1

        return drop_index


if __name__ == '__main__':
    print(RemoveElement().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
