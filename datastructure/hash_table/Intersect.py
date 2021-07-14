#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/2 22:38
# @File    : Intersect.py
"""
给定两个数组，编写一个函数来计算它们的交集。
"""
from typing import List


class Intersect(object):

    def __init__(self):
        pass

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        交集，排序双指针做法，可以适用于大数据集，将排序改为归并排序，双指针读取2个文件，对比

        时间复杂度O(max(logN, logM, M + N))
        空间复杂度O(min(N, M))
        :param nums1:
        :param nums2:
        :return:
        """
        nums1.sort()
        nums2.sort()
        intersect_result = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                intersect_result.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1

        return intersect_result

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        哈希表做法
        :param nums1:
        :param nums2:
        :return:
        """
        hash_map = dict()
        for i in range(len(nums1)):
            hash_map.setdefault(nums1[i], 0)
            hash_map[nums1[i]] += 1

        intersect_result = []
        for j in range(len(nums2)):
            if hash_map.get(nums2[j], 0) > 0:
                intersect_result.append(nums2[j])
                hash_map[nums2[j]] -= 1
                if hash_map[nums2[j]] == 0:
                    hash_map.pop(nums2[j])

        return intersect_result


if __name__ == '__main__':
    print(Intersect().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
