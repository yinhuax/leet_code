#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/11 18:06
# @File    : Subsets.py
from typing import List

"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法
        :param nums:
        :return:
        """
        result = []
        n = len(nums)

        def dfs(index, cur):
            result.append(cur)
            if index >= n:
                return

            for i in range(index, n):
                dfs(i + 1, cur + [nums[i]])

        dfs(0, [])
        return result


if __name__ == '__main__':
    print(Solution().subsets(nums=[1, 2, 3]))
