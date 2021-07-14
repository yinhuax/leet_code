#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/14 11:18
# @File    : MajorityElement.py
from typing import List

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        """
        计数方法，时间复杂度O(N), 空间复杂度O(N)
        :param nums:
        :return:
        """
        num_counter = dict()
        for num in nums:
            num_counter.setdefault(num, 0)
            num_counter[num] += 1

        return [k for k, v in num_counter.items() if v > int(len(nums) / 2)][0]

    def majorityElement1(self, nums: List[int]) -> int:
        """
        排序，取n//2 处数据
        :param nums:
        :return:
        """
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    print(Solution().majorityElement1([2, 2, 1, 1, 1, 2, 2]))
