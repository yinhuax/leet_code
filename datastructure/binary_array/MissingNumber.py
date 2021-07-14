#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/5 23:38
# @File    : MissingNumber.py
from typing import List

"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    print(Solution().missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
