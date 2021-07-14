#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 18:19
# @File    : FindMedianSortedArrays.py
from typing import List


class FindMedianSortedArrays(object):

    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        双指针，遍历 (m + n - 1) // 2 就是中位数
        :param nums1:
        :param nums2:
        :return:
        """
        m = len(nums1)
        n = len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)

        left = right = -1
        a_start = b_start = 0
        for i in range((m + n) // 2 + 1):
            left = right
            if a_start < m and (b_start >= n or nums1[a_start] < nums2[b_start]):
                right = nums1[a_start]
                a_start += 1
            else:
                right = nums2[b_start]
                b_start += 1

        if (m + n) % 2 == 0:
            return (left + right) / 2
        else:
            return right

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        二分查找，中位数左边的个数等于右边个数
        :param nums1:
        :param nums2:
        :return:
        """
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays1(nums2, nums1)

        k = (m + n + 1) // 2
        left, right = 0, n
        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                # 不满足条件
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float('-inf'), nums2[m2 - 1] if m2 > 0 else float('-inf'))
        if (m + n) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n else float('inf'), nums2[m2] if m2 < m else float('inf'))
        return (c1 + c2) / 2


if __name__ == '__main__':
    print(FindMedianSortedArrays().findMedianSortedArrays1(nums1=[1, 3], nums2=[2]))
