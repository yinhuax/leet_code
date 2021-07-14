#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 21:58
# @File    : FindRestaurant.py
from typing import List


class FindRestaurant(object):

    def __init__(self):
        pass

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        使用一个哈希表存储，时间复杂度O(N + M)，空间复杂度O(N + M - 1)
        :param list1:
        :param list2:
        :return:
        """
        hash_table = dict()
        for i in range(len(list1)):
            hash_table[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in hash_table:
                hash_table[list1[j]] += j

        insect = set(list1) & set(list2)
        min_index_sums = min([hash_table[k] for k in insect])

        return [k for k in insect if hash_table[k] == min_index_sums]

    def findRestaurant1(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        pythonic 写法
        :param list1:
        :param list2:
        :return:
        """
        d = {k: list1.index(k) + list2.index(k) for k in set(list1) & set(list2)}
        return [x for x in d if d[x] == min(d.values())]


if __name__ == '__main__':
    print(FindRestaurant().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                          ["KFC", "Burger King", "Tapioca Express", "Shogun"]))
