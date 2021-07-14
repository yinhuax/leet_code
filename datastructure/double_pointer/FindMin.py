#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/31 11:03
# @File    : FindMin.py
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

 

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c3ki5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


class FindMin(object):

    def __init__(self):
        pass

    def findMin(self, nums: List[int]) -> int:
        """
        遍历方式，时间复杂度O(n)
        :param nums:
        :return:
        """
        min_value = 5001
        for i in range(len(nums)):
            min_value = min(min_value, nums[i])
        return min_value

    def findMin1(self, nums: List[int]) -> int:
        """
        二分查找方式
        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == '__main__':
    print(FindMin().findMin1([3, 4, 5, 1, 2]))
