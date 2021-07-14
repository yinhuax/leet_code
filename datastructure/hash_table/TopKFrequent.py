#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/5 1:39
# @File    : TopKFrequent.py
from typing import List


class TopKFrequent(object):

    def __init__(self):
        pass

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        使用哈希表
        :param nums:
        :param k:
        :return:
        """
        # 记录出现的次数
        lookup = dict()
        for i in nums:
            lookup.setdefault(i, 0)
            lookup[i] += 1

        # 按出现次数逆序排序
        lookup = sorted(lookup.items(), key=lambda x: -x[1])
        return [k for k, v in lookup][:k]


if __name__ == '__main__':
    print(TopKFrequent().topKFrequent(nums=[3, 0, 1, 0], k=1))
