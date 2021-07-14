#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/28 23:48
# @File    : FindMaxConsecutiveOnes.py
from typing import List

"""
LC 最大连续1的个数

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/cd71t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class FindMaxConsecutiveOnes(object):

    def __init__(self):
        pass

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        双指针，空间复杂度O(2), 时间复杂度O(N)
        :param nums:
        :return:
        """
        max_nums = 0
        start = 0
        for i in range(len(nums)):
            if nums[i]:
                start += 1
            else:
                max_nums = max(max_nums, start)
                start = 0

        max_nums = max(max_nums, start)
        return max_nums


if __name__ == '__main__':
    print(FindMaxConsecutiveOnes().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
