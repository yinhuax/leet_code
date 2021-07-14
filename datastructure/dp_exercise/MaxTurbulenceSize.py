#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/22 8:23
# @File    : MaxTurbulenceSize.py
from typing import List

"""
当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        动态规划：如果当前为下降状态： down = up + 1
                如果当前为上升状态： up = down + 1
                res = max(res, down, up)
        :param arr:
        :return:
        """
        res = 1
        up = 1
        down = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                # 上升状态
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                # 下降状态
                down = up + 1
                up = 1
            else:
                down = up = 1
            res = max(res, max(down, up))

        return res
