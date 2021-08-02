#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/2 15:21
# @File    : FindRightInterval.py
from typing import List

"""
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-right-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        二分查找
        """

        # 先对数组进行排序，用inx 记录原始下标
        sorted_nums = sorted([(intervals[i][0], i) for i in range(len(intervals))], key=lambda x: x[0])

        ans = []
        for i in range(len(intervals)):
            left = 0
            right = len(intervals) - 1

            target = intervals[i][1]
            idx = -1
            while left < right:
                mid = (left + right) >> 1

                # start_i >= end_j
                if sorted_nums[mid][0] >= target:
                    idx = sorted_nums[mid][1]
                    right = mid
                else:
                    left = mid + 1

            if sorted_nums[left][0] >= target:
                idx = sorted_nums[left][1]

            ans.append(idx)

        return ans

