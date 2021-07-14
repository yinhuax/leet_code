#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2020/12/20 17:05
# @File    : FindTargetSumWays.py

"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/queue-stack/ga4o2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
from typing import List


class FindTargetSumWays(object):

    def __init__(self):
        pass

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 记忆化dfs
        # from functools import lru_cache

        # @lru_cache
        visited = dict()

        def dfs(i, sum_result, visited):
            if i < len(nums) and (i, sum_result) not in visited:
                visited[(i, sum_result)] = dfs(i + 1, sum_result - nums[i], visited) + \
                                           dfs(i + 1, sum_result + nums[i], visited)

            return visited.get((i, sum_result), sum_result == S)

        return dfs(0, 0, visited)

    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1): dp[j] += dp[j - num]
        return dp[P]

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        length, dp = len(nums), {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)


if __name__ == '__main__':
    print(FindTargetSumWays().findTargetSumWays([1, 1, 1, 1, 1], 3))
