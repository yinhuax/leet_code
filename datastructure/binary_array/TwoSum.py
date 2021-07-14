#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/10 15:54
# @File    : TwoSum.py
from typing import List

"""
给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/binary-search/xeqevt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class TwoSum(object):

    def __init__(self):
        pass

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        哈希表做法，空间复杂度O(N), 时间复杂度O(M)
        :param numbers:
        :param target:
        :return:
        """
        seen = dict()
        for i, j in enumerate(numbers):
            if target - j not in seen:
                seen[j] = i
            else:
                return [seen[target - j] + 1, i + 1]

        return [-1, -1]

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        """
        双指针做法
        :param numbers:
        :param target:
        :return:
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left + 1, right + 1]
            elif sums > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """
        二分查找算法
        :param numbers:
        :param target:
        :return:
        """
        for i in range(len(numbers)):
            target1 = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if target1 == numbers[mid]:
                    return [i + 1, mid + 1]
                elif target1 > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return [-1, -1]


if __name__ == '__main__':
    print(TwoSum().twoSum(numbers=[2, 3, 4], target=6))
