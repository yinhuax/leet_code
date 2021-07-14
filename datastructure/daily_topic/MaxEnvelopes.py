#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/3/4 6:44
# @File    : MaxEnvelopes.py
from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        二分查找，时间复杂度O(nlogn)
        :param envelopes:
        :return:
        """
        import bisect
        if not envelopes:
            return 0

        # 对数组排序
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > f[-1]:
                f.append(envelopes[i][1])
            else:
                index = self.binary_search_left(f, envelopes[i][1])
                # index = bisect.bisect_left(f, envelopes[i][1])
                f[index] = envelopes[i][1]

        return len(f)

    def binary_search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def binary_search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return left

    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        """
        动态规则写法
        :param envelopes:
        :return:
        """
        if not envelopes:
            return 0

        # 对数组排序
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    print(Solution().maxEnvelopes([[5, 4], [6, 5], [6, 7], [2, 3]]))
