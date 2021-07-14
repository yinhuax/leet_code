#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/16 10:21
# @File    : CombinationSum.py
from typing import List

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯算法
        :param candidates:
        :param target:
        :return:
        """

        def callbacks(start, end, path, target):
            if target == 0:
                res.append(path)

            for i in range(start, end):
                diff = target - candidates[i]
                # 后面的数都比当前大，可以结束遍历
                if diff < 0:
                    return
                callbacks(i, end, path + [candidates[i]], diff)

        res = []
        # 对数组进行排序，可以剪掉部分枝
        if len(candidates) < 1:
            return res

        candidates.sort()
        callbacks(0, len(candidates), [], target)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
