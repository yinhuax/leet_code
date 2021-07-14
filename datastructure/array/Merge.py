#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/9 21:21
# @File    : Merge.py
from typing import List

"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

 

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-array/x9lhe7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Merge(object):

    def __init__(self):
        pass

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        使用双指针，先逆序排序，然后排序，空间复杂度O(1), 时间复杂度max(O(m + n), O(log(m + n)))，从前往后遍历
        
        无法完成
        """
        p = m + n - 1
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            # 判断
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p -= 1

        if p2 < n:
            nums1[:n - p2] = nums2[p2:]
        elif p1 < m:
            nums1[:m - p1] = nums1[p1:m]

        nums1.sort()
        print(nums1)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        双指针，从后往前遍历
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]


if __name__ == '__main__':
    print(Merge().merge1(nums1=[1, 2, 4, 5, 6, 0], m=5, nums2=[3], n=1))
