#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 11:56
# @File    : MoveZeroes.py
from typing import List


class MoveZeroes(object):

    def __init__(self):
        pass

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        双指针
        """
        first = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[first] = nums[i]
                first += 1

        for i in range(first, len(nums)):
            nums[i] = 0

    def moveZeroes1(self, nums: List[int]) -> None:
        left = right = 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


if __name__ == '__main__':
    print(MoveZeroes().moveZeroes1([0, 1, 0, 3, 12]))
