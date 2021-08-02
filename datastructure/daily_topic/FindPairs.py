#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/8/2 7:16
# @File    : FindPairs.py
"""
给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
注意，|val| 表示 val 的绝对值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-diff-pairs-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        """
        计数法
        :param nums:
        :param k:
        :return:
        """
        from collections import Counter
        couter = Counter(nums)

        res = 0
        for c in couter:
            if (k > 0 and (c + k in couter)) or (k == 0 and couter[c] > 1):
                res += 1

        return res

    def findPairs1(self, nums: List[int], k: int) -> int:
        """
        二分查找法
        :param nums:
        :param k:
        :return:
        """
        # 排序
        nums = sorted(nums)

        res = 0
        for i in range(len(nums)):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = k + nums[i]
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    res += 1
                    break

        return res


if __name__ == '__main__':
    print(Solution().findPairs1(nums=[3, 1, 4, 1, 5], k=2))
