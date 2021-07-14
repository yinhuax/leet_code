#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/11 15:55
# @File    : Insert.py
from typing import List

"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
"""


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        插入区间
        :param intervals:
        :param newInterval:
        :return:
        """
        ans = []
        for i, inter in enumerate(intervals):
            if inter[1] < newInterval[0]:
                ans.append(inter)
            elif inter[0] > newInterval[1]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                break
            # inter[0] < newInterval[1] and inter[1] > newInterval[0]，包含关系
            else:
                # 区间合并
                if inter[0] < newInterval[0]:
                    newInterval[0] = inter[0]
                if inter[1] > newInterval[1]:
                    newInterval[1] = inter[1]
        else:
            ans.append(newInterval)

        return ans


if __name__ == '__main__':
    print(Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
