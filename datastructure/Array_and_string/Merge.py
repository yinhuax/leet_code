#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/1/16 21:09
# @File    : Merge.py

"""
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c5tv3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


class Merge(object):

    def __init__(self):
        pass

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        按第一个元素排序数组
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，就可以与上一区间合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    # 手写快排算法
    def quick_sort(self, nums: List[List[int]], l, r):
        if l < r:
            pivot = self.partition(nums, l, r)

            self.partition(nums, l, pivot - 1)
            self.partition(nums, pivot + 1, r)
        return nums

    def partition(self, nums, l, r):
        """
        快速排序算法
        :param nums:
        :param l:
        :param r:
        :return:
        """
        pivot = nums[l]
        while l < r:
            # 先从右往左扫描，找到比基准值小的
            while l < r and nums[r][0] >= pivot[0]:
                r -= 1
            # 找到第一个比基准小的交换位置
            nums[l] = nums[r]

            # 然后从右往左扫描
            while l < r and nums[l][0] <= pivot[0]:
                l += 1
            nums[r] = nums[l]

        nums[l] = pivot
        return l


if __name__ == '__main__':
    nums = [[2, 3], [1, 6], [8, 10], [15, 18]]
    print(Merge().quick_sort(nums, 0, len(nums) - 1))
