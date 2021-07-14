#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/6/11 11:17
# @File    : ThreeSumClosest.py
from typing import List

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        最接近的三数之和
        解题思路：排序 + 双指针
        :param nums:
        :param target:
        :return:
        """
        nums.sort()

        def update(cur):
            nonlocal best
            if abs(best - target) > abs(cur - target):
                best = cur

        # 双指针
        best = 10 ** 7
        # a, b, c  枚举a，双指针扫描b, c，排序关系a < b < c
        for i in range(len(nums)):
            # 跳过重复扫描值
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k, j = i + 1, len(nums) - 1
            while k < j:
                sums = nums[i] + nums[k] + nums[j]
                if sums == target:
                    return target

                update(sums)
                if sums > target:
                    # 如果和大于target，移动c
                    j0 = j - 1
                    # 移动到下一个不相等的元素
                    while k < j0 and nums[j] == nums[j0]:
                        j0 -= 1
                    j = j0
                else:
                    # 如果和小于target，移动b对应的指针
                    k0 = k + 1
                    # 移动到下一个不相等的元素
                    while k0 < j and nums[k0] == nums[k]:
                        k0 += 1
                    k = k0

        return best


if __name__ == '__main__':
    # 测试
    print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
