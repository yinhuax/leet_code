#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/25 23:49
# @File    : TwoSum.py
from typing import List

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/cnkjg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TwoSum(object):

    def __init__(self):
        pass

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                # 当前数之和大于target，目标值位于左边
                right = right - 1
            elif cur_sum < target:
                left = left + 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]


if __name__ == '__main__':
    print(TwoSum().twoSum(numbers=[5, 25, 75], target=100))
