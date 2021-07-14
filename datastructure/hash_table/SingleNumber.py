#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 14:28
# @File    : SingleNumber.py
from typing import List


class SingleNumber(object):

    def __init__(self):
        pass

    def singleNumber(self, nums: List[int]) -> int:
        """
        位运算
        :param nums:
        :return:
        """
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]

        return result
