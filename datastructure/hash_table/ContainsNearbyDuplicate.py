#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 23:05
# @File    : ContainsNearbyDuplicate.py
"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/hash-table/xx5bzh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
from typing import List


class ContainsNearbyDuplicate(object):

    def __init__(self):
        pass

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        哈希表
        :param nums:
        :param k:
        :return:
        """
        hash_table = dict()
        for i in range(len(nums)):
            if nums[i] in hash_table and i - hash_table[nums[i]] <= k:
                return True
            hash_table[nums[i]] = i

        return False
