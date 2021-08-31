#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/31 0:54
# @File    : CorpFlightBookings.py
from typing import List

"""
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/corporate-flight-bookings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        前缀和
        :param bookings:
        :param n:
        :return:
        """
        import numpy as np
        result = np.array([0] * n)
        for i, j, value in bookings:
            result[i - 1: j] += value

        return result.tolist()

    def corpFlightBookings1(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        差分做法
        :param bookings:
        :param n:
        :return:
        """
        result = [0] * n
        for left, right, value in bookings:
            result[left - 1] += value
            if right < n:
                result[right] -= value

        for i in range(1, n):
            result[i] += result[i - 1]
        return result


if __name__ == '__main__':
    print(Solution().corpFlightBookings1(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
