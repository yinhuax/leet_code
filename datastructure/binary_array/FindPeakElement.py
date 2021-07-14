#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 10:16
# @File    : FindPeakElement.py
from typing import List

"""
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xem7js/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class FindPeakElement(object):

    def findPeakElement(self, nums: List[int]) -> int:
        """
        二分查找
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(FindPeakElement().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
