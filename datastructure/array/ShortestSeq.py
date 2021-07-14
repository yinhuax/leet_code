#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/1 6:11
# @File    : ShortestSeq.py
from typing import List

"""
假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。

返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-supersequence-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        """
        滑动窗口，转换为字典，记录当前窗口所有数字出现次数
        :param big:
        :param small:
        :return:
        """
        small_dict = {}
        for num in small:
            small_dict.setdefault(num, 0)

        counter = 0
        left, right = 0, 0
        # 分别对应左，当前窗口长度
        result = [0, float('inf')]
        while right < len(big):
            if big[right] not in small_dict:
                right += 1
                continue

            if small_dict.get(big[right], -1) == 0:
                counter += 1

            small_dict[big[right]] += 1

            right += 1
            while counter == len(small_dict):
                # 收缩左窗口
                if right - left < result[1]:
                    result[0] = left
                    result[1] = right - left

                # 左边收缩
                if big[left] in small_dict:
                    small_dict[big[left]] -= 1
                    if small_dict[big[left]] == 0:
                        counter -= 1
                left += 1

        if result[1] == float('inf'):
            return []

        return [result[0], result[0] + result[1] - 1]


if __name__ == '__main__':
    big = [1, 2, 3]
    small = [4]
    print(Solution().shortestSeq(big, small))
