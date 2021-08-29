#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/30 6:44
# @File    : PickIndex.py
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        # 初始化概率数组
        n = len(w)
        sums = sum(w)
        w_pro = [0] * n
        pre_pro_sum = 0
        for i in range(n):
            pre_pro_sum += w[i]
            w_pro[i] = pre_pro_sum / sums
        self.pro_arr = w_pro

    def binary_search(self, target, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

    def pickIndex(self) -> int:
        import random
        # 随机一个概率
        target = random.random()
        # 从概率数组找到
        return self.binary_search(target, self.pro_arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
