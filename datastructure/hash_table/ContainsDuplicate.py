#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 14:14
# @File    : ContainsDuplicate.py
from typing import List


class ContainsDuplicate(object):

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)