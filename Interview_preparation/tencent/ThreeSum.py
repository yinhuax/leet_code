#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 8:11
# @File    : ThreeSum.py
from typing import List

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        排序 + 双指针
        :param nums:
        :return:
        """
        result = []
        nums.sort()
        n = len(nums)

        for first in range(n):
            # 跳过重复的三元组。
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            target = -nums[first]
            third = n - 1
            for second in range(first + 1, n):
                # 需要和上次枚举的数不同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 保证second指针在third的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                # 如果指针重合，不存在a + b + c = 0 且 b < c的数据
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    result.append([nums[first], nums[second], nums[third]])

        return result
