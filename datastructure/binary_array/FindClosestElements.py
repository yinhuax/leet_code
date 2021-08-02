#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/2 15:47
# @File    : FindClosestElements.py
from typing import List

"""
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-closest-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        保留 k 个差值最小元素
        :param arr:
        :param k:
        :param x:
        :return:
        """

        # 移除 len(arr) - k 个元素
        left = 0
        right = len(arr) - 1

        remove_size = len(arr) - k
        while remove_size > 0:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1

            remove_size -= 1

        return arr[left: left + k]

    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        二分查找
        :param arr:
        :param k:
        :param x:
        :return:
        """
        left = 0
        # 定位左边界
        right = len(arr) - k

        while left < right:
            mid = (left + right) >> 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]


if __name__ == '__main__':
    print(Solution().findClosestElements1(arr=[1, 1, 2, 2, 2, 2, 2, 3, 3], k=3, x=3))
