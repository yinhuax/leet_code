#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 16:29
# @File    : ContainsNearbyAlmostDuplicate.py
from typing import List


class ContainsNearbyAlmostDuplicate(object):

    def __init__(self):
        pass

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        滑动窗口，使用set 存储k个元素
        :param nums:
        :param k:
        :param t:
        :return:
        """
        memo = set()
        for i in range(len(nums)):
            if t == 0:
                if nums[i] in memo:
                    return True
            else:
                for pre in memo:
                    if abs(nums[i] - pre) <= t:
                        return True

            memo.add(nums[i])
            if len(memo) > k:
                memo.remove(nums[i - k])

        return False
