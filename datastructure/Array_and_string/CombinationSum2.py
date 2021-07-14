#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/11 14:51
# @File    : CombinationSum2.py
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯算法
        :param candidates:
        :param target:
        :return:
        """
        n = len(candidates)

        all_result = []
        candidates.sort()
        def backtrack(index, result: List[int], sums):
            if sums > target:
                return

            if sums == target:
                all_result.append(result)
                return

            for i in range(index, n):
                # 跳过重复数字
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # 剪枝优化
                if sums + candidates[i] <= target:
                    backtrack(i + 1, result + [candidates[i]], sums + candidates[i])

        backtrack(0, [], 0)
        return all_result


if __name__ == '__main__':
    print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
