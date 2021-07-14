#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 6:09
# @File    : TwoSum.py
from typing import List


class TwoSum(object):

    def __init__(self):
        pass

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        使用哈希表
        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left + 1, right + 1]
            elif sums > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]
