#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/11 8:58
# @File    : FourSum.py
from typing import List

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/all-about-lockup-table/xh5n2t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        回溯算法，超时
        :param nums:
        :param target:
        :return:
        """
        import numpy as np
        result = []

        def backtrack(total, res, index, sums):
            if total == 4 and sum(res) == target:
                result.append(res[:])
                return

            # 回溯加剪枝
            for i in range(index, len(nums)):
                next_sum = sums + nums[i]
                if total >= 4 or (next_sum > 0 and next_sum > target):
                    break
                res.append(nums[i])
                backtrack(total + 1, res, i + 1, next_sum)
                res.pop(-1)

        nums.sort()
        backtrack(0, [], 0, 0)
        return np.array(list(set([tuple(t) for t in result]))).tolist()

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        双指针+哈希表
        :param nums:
        :param target:
        :return:
        """
        result = []
        if not nums or len(nums) < 4:
            return result

        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            # 过滤重复情况
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 已经大于 target，不需要再遍历
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 当前最大和小于target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # 过滤重复值
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


if __name__ == '__main__':
    print(Solution().fourSum1([-1, 0, 1, 2, -1, -4], -1))
