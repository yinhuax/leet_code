#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 7:06
# @File    : ThreeSum.py
from typing import List

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-lockup-table/xhhlwv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
import numpy as np


class ThreeSum(object):

    def __init__(self):
        pass

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和 or N 数之和，回溯算法方式，超时
        :param nums:
        :return:
        """
        import numpy as np
        result = []

        def backtrack(total, res, index):
            if total == 3 and sum(res) == 0:
                result.append(res[:])
                return

            # 回溯加剪枝
            for i in range(index, len(nums)):
                if total >= 3 or sum(res) > 0:
                    break
                res.append(nums[i])
                backtrack(total + 1, res, i + 1)
                res.pop(-1)

        nums.sort()
        backtrack(0, [], 0)
        return np.array(list(set([tuple(t) for t in result]))).tolist()

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        """
        排序+双指针
        :param nums:
        :return:
        """
        nums.sort()
        n = len(nums)
        result = []

        # 枚举
        for first in range(n):
            # 需要和上次枚举的数不一样
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # 对应的指针初始指向数组的最右端
            third = n - 1
            target = 0 - nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                # 如果指针重合
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    result.append([nums[first], nums[second], nums[third]])

        return result


if __name__ == '__main__':
    print(ThreeSum().threeSum([-1, 0, 1, 2, -1, -4]))
