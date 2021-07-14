#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 10:54
# @File    : FindMin.py
from typing import List

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xeawbd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class FindMin(object):

    def __init__(self):
        pass

    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right - left) // 2 + left
            # 位于左半边数组上
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

    def findMin1(self, nums: List[int]) -> int:
        """
        找到最小值，从重复数组当中，每次遍历左边界值
        :param nums:
        :return:
        """
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right - left) // 2 + left
            # 位于最小值右侧数组上
            if nums[mid] < nums[right]:
                right = mid
            # 位于最小值左侧数组上
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':
    print(FindMin().findMin1([10, 1, 10, 10, 10]))
