#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/5 23:57
# @File    : HIndex.py
from typing import List

"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        """
        二分查找，判断当前h Index是否符合条件：满足 (len(citations) - h_index) >= citations[h_index]
        :param citations:
        :return:
        """
        if not citations or citations[-1] == 0:
            return 0

        left, right = 0, len(citations) - 1
        while left < right:
            h_index = left + (right - left) // 2
            if (len(citations) - h_index) <= citations[h_index]:
                right = h_index
            else:
                left = h_index + 1

        return len(citations) - left


if __name__ == '__main__':
    print(Solution().hIndex(citations=[0]))
