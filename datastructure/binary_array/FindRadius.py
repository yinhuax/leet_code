#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/7 22:54
# @File    : FindRadius.py
from typing import List

"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/heaters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        查找最大半径，思路：二分查找，找到每个房子离加速器最近的距离，从所有距离中选择一个最远的即结果
        :param houses:
        :param heaters:
        :return:
        """
        res = []
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
        for c in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = left + right >> 1
                if heaters[mid] < c:
                    left = mid + 1
                else:
                    right = mid
            res.append(min(c - heaters[left - 1], heaters[left] - c))

        return max(res)
