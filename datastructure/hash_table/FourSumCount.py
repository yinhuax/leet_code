#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Mike
# @Contact : 597290963@qq.com
# @Time    : 2021/2/5 0:43
# @File    : FourSumCount.py
from typing import List


class FourSumCount(object):

    def __init__(self):
        pass

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        分组哈希
        :param A:
        :param B:
        :param C:
        :param D:
        :return:
        """

        lookup = dict()
        for i in A:
            for j in B:
                sums = i + j
                lookup.setdefault(sums, 0)
                # 出现次数+1
                lookup[sums] += 1

        ans = 0
        for n in C:
            for m in D:
                if -(n + m) in lookup:
                    ans += lookup[-(n + m)]

        return ans

    def fourSumCount1(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        分组，二分法
        :param A:
        :param B:
        :param C:
        :param D:
        :return:
        """
        # 使用两个数组分别存储A+B、C+D的和
        first_list = list()
        for i in A:
            for j in B:
                first_list.append(i + j)

        second_list = list()
        for n in C:
            for m in D:
                second_list.append(n + m)

        # 对第二个数组排序
        second_list.sort()

        ans = 0
        # 对第一个分组和变量，从第二个分组和中使用二分查找搜索，搜索左边界值和右边界值
        for i in first_list:
            l_index = self.l_bound_binary_search(-i, second_list)
            r_index = self.r_bound_binary_search(-i, second_list)

            if l_index != -1 and r_index != -1:
                ans += (r_index - l_index + 1)
        return ans

    def l_bound_binary_search(self, target, nums):
        """
        二分查找搜索左边界值
        :param target:
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid

        if nums[left] != target:
            return -1

        return left

    def r_bound_binary_search(self, target, nums):
        """
        二分查找搜索右边界值
        :param target:
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left + 1) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        if nums[left] != target:
            return -1

        return left


if __name__ == '__main__':
    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    print(FourSumCount().fourSumCount1(A, B, C, D))
