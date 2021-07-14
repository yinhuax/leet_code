#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/15 18:17
# @File    : MajorityElement2.py
from typing import List

"""
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

 

示例 1：

输入：[3,2,3]
输出：[3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        求众数，排序，用一个数标记连续重复的长度
        :param nums:
        :return:
        """
        if not nums or len(nums) < 3:
            return list(set(nums))

        max_len = 1
        nums.sort()

        result = set()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # 数据连续
                max_len += 1
                if max_len > (len(nums) // 3):
                    result.add(nums[i])
            else:
                # 不连续，重置
                max_len = 1

        return list(result)


if __name__ == '__main__':
    print(Solution().majorityElement([1, 2]))
