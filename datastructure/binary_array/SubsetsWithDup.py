#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/13 21:34
# @File    : SubsetsWithDup.py
from typing import List

"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法
        :param nums:
        :return:
        """
        result = []

        nums.sort()
        def dfs(index, cur_arr):
            result.append(cur_arr[:])
            # 剪枝优化
            if index >= len(nums):
                return

            for i in range(index, len(nums)):
                if i > index and nums[i - 1] == nums[i]:  # 判断，避免重复利用的情况
                    continue
                dfs(i + 1, cur_arr + [nums[i]])

        dfs(0, [])

        return result


if __name__ == '__main__':
    print(Solution().subsetsWithDup(nums=[4, 4, 4, 1, 4]))
