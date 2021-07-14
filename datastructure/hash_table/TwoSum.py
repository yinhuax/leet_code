#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 21:18
# @File    : TwoSum.py
from typing import List


class TwoSum(object):

    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表写法
        :param nums:
        :param target:
        :return:
        """
        # 使用map存储已经遍历过的值
        hash_map = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[nums[i]] = i


if __name__ == '__main__':
    print(TwoSum().twoSum(nums=[3, 2, 4], target=6))
